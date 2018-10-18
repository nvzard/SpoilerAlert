import re

from Utils.colors import print_string
from Utils.database import feed_data_into_db
from Utils.emailer import send_email_to_user
from TVShow.TVShow import TVShow

from colorama import init
from itertools import cycle
from multiprocessing.dummy import Pool as ThreadPool


NO_OF_WORKERS = 4


def get_input(text):
    """
    Get input from user.

    :param text: Text to print before taking input.

    :return:     Input of user.
    """
    return input(text)

def get_tv_shows_list():
    """
    Get list of TV shows as string input from user.
    Then clean the input and convert the sting in a list.
    
    :return: list of TV shows
    """
    INPUT_STRING = 'Enter the list of TV shows seperated by comma(,): '
    tv_shows = [x.strip().lower() for x in get_input(INPUT_STRING).split(',')]
    return tv_shows

def get_user_input():
    """
    Get input of user's email and list of TV Shows from command-line

    :return: user's email, list of TV shows requested by user
    """
    email_id = get_input("Enter your e-mail address: ")
    email_id = validate_email(email_id)

    tv_shows = get_tv_shows_list()
    return email_id, tv_shows

def validate_email(email):
    """
    Validate user_email by matching againt email RegEx.
    Exit if email is invalid.

    :param email: Email of user

    :return: Validated email address
    """
    if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
        print('Email address ' + email + ' is not valid.')
        exit(1)

    return email

def get_show_status(tv_show_name):
    """
    Get data regarding the next episode

    :param tv_show_name: Name of TV Show

    :return: Response/Result after fetching the data from internet
    """
    return TVShow(tv_show_name).status

def processing(tv_show_list):
    """
    Process and get the results for all the shows in the list

    :param tv_show_list: List of all the TV Shows

    :return: list of processed final responses for every TV Show
    """
    # Make the Pool of workers
    pool = ThreadPool(NO_OF_WORKERS)

    # Fetches the status of TV shows in their own threads
    # and return the results
    results = pool.map(get_show_status, tv_show_list)

    # close the pool and wait for the work to finish
    pool.close()
    pool.join()

    return results

def main():
    """
    Function which controls the flow of application.
    It gets executed first.

    Sequence of operations:
    1. Fetch user input (email, list of TV Shows).
    2. Feed data into database.
    3. Fetch and process TV Show information from the internet.
    4. Format and print the status of TV shows on the command-line.
    5. Send the generated results to the user via email.
    6. Exit gracefully.
    """
    # Initiate colorama for colourful output
    init()
    # Iterator to toggle b/w 2 colours
    colour_alternator = cycle(range(2))
    # Initial body of email to be sent to user
    email_body = ''
    # Get email and list of TV Shows as input from user
    user_email, tv_show_list = get_user_input()
    # Record interaction in the data base along with inputs and timestamp
    feed_data_into_db(user_email, tv_show_list)
    # Fetch results for the list of TV Shows
    results = processing(tv_show_list)

    for idx, tv_show_response in enumerate(results):
        stdout_str = str(idx+1) + '> ' + tv_show_response
        # Print the status of each show on the terminal
        print_string(stdout_str, colour_alternator)
        # Append the status of each sting in the email body
        email_body += stdout_str

    # Send the status of TV Shows to the user via E-Mail
    send_email_to_user(user_email, email_body)
    # Exit Gracefully
    exit(0)

if __name__ == "__main__":
    main()
