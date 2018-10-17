import random
from colorama import Fore, Style


CYAN = Fore.CYAN + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
color_combination = [CYAN, BLUE]


def print_string(string, colour_alternator):
    """
    Print a coloured string

    :param string: String that needs to be printed
    :param colour_alternator: Iterate to toggle b/w colours
    """

    if string.find('**ERROR**') == -1:
        # Toogle b/w two colours
        color = color_combination[next(colour_alternator)]
    else:
        # Set color to RED if there is error in the TV Show status
        color = RED
    # Print the string and reset so that a different colour can be printed
    print(color + string + Style.RESET_ALL)
