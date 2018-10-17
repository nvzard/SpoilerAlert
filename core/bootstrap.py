import re

from TVShow.TVShow import TVShow
from database import feed_data_into_db
from emailer import send_email_to_user
from colors import print_string

from colorama import init
from itertools import cycle
from multiprocessing.dummy import Pool as ThreadPool



NO_OF_WORKERS = 4

def get_tv_shows_list():
    """
    Takes and cleans the user input.
    
    Return: list of tv shows
    """
    INPUT_STRING = 'Enter the list of TV shows seperated by comma(,): '
    tv_shows = [x.strip().lower() for x in input(INPUT_STRING).split(',')]
    return tv_shows

def get_user_input():
    email_id = input("Enter your e-mail address: ")
    email_id = validate_email(email_id)

    tv_shows = get_tv_shows_list()
    return email_id, tv_shows

def validate_email(email):
    if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
        print('Email address ' + email + ' is not valid.')
        exit(1)

    return email

def get_show_response(show_name):
    return TVShow(show_name).response

def processing(tv_show_list):
    # Make the Pool of workers
    pool = ThreadPool(NO_OF_WORKERS)

    # Fetches the status of TV shows in their own threads
    # and return the results
    results = pool.map(get_show_response, tv_show_list)

    # close the pool and wait for the work to finish
    pool.close()
    pool.join()

    return results

def main():
    init()
    colour_alternator = cycle(range(2))
    email_body = ''

    user_email, tv_show_list = get_user_input()
    feed_data_into_db(user_email, tv_show_list)

    results = processing(tv_show_list)

    for idx, tv_show_response in enumerate(results):
        stdout_str = str(idx+1) + '> ' + tv_show_response
        email_body += stdout_str
        print_string(stdout_str, colour_alternator)

    send_email_to_user(user_email, email_body)
    exit(0)

if __name__ == "__main__":
    main()