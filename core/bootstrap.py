import re

from colorama import init
from TVShow.TVShow import TVShow
from database import feed_data_into_db
from emailer import send_email_to_user
from colors import print_string
from itertools import cycle


def validate_email(email):
    if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
        print('Email address ' + email + ' is not valid.')
        exit(1)

    return email

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

def main():
    init()
    colour_alternator = cycle(range(2))
    email_body = ''

    user_email, tv_show_list = get_user_input()
    feed_data_into_db(user_email, tv_show_list)

    for idx, show_name in enumerate(tv_show_list):
        stdout_str = str(idx+1) + '> ' + TVShow(show_name).response
        email_body += stdout_str
        print_string(stdout_str, colour_alternator)

    send_email_to_user(user_email, email_body)
    exit(0)

if __name__ == "__main__":
    main()