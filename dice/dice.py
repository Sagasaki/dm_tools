##
## Dice rolling tool
## Copyright 2018 Jared C. Allen
##

"""
This tool outputs the result of a dice roll based on inputs of the
die type and any multipliers or modifiers (2d6, 1d4+3, etc).
"""

import random
import re
from colorama import Fore, Style

def die_roll():
    """Dice roll engine"""
    die_input = input("Specify die roll in format '2d6': ").split("d")
    die = [int(value) for value in die_input]
    result = 0
    for x in range (0, die[0]):
        result = result + random.randint(1, die[1])
    print(Fore.GREEN + "Rolling %i d %i... " % (die[0], die[1]) + str(result), Style.RESET_ALL)

#while True:
#        die_roll()

def die_roll2():
    """Dice roll engine"""
    die_input = input("Specify die roll in format '2d6+3': ")
    die = [int(x) for x in re.findall('\\d+', die_input)]
    result = 0
    for y in range (0, die[0]):
        result = result + random.randint(1, die[1])
    if '+' in die_input:
        result = result + die[2]
    elif '-' in die_input:
        result = result - die[2]
    print(Fore.GREEN + "Rolling %i d %i... " % (die[0], die[1]) + str(result), Style.RESET_ALL)

while True:
        die_roll2()

