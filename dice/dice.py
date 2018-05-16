##
## Dice rolling tool
## Copyright 2018 Jared C. Allen
##

"""
This tool outputs the result of a dice roll based on inputs of the
die type and any multipliers or modifiers (2d6, 1d4+3, etc).
"""

import random
from colorama import Fore, Style

def roll_die():
    """Dice roll engine"""
    die = int(input("Select die: ->d2, d4, d6, d8, d10, d12, d20, or d100 (# only): "))
    if die not in [2, 4, 6, 8, 10, 12, 20, 100]:
        print(Fore.RED + "Invalid die type. Please roll again.", Style.RESET_ALL)
        return
    print(Fore.GREEN + "Rolling a d%i... " % (die), + random.randint(1, die), Style.RESET_ALL)

while True:
    roll_die()
