import random
from colorama import Fore, Style


CYAN = Fore.CYAN + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
color_combination = [CYAN, BLUE]


def print_string(string, colour_alternator):
	if string.find('**ERROR**') == -1:
		color = color_combination[next(colour_alternator)]
	else:
		color = RED
	print(color + string + Style.RESET_ALL)