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

def die_roller():
    """Dice roll engine"""
    die_input = input("Specify die roll in format '2d6(+/-)3': ")
    if die_input == 'q':
        print("Thank you for using the D&D Dice Roller. Goodbye!\n")
        return
    else:
        die = [int(x) for x in re.findall('\\d+', die_input)]
        try:
            if len(die) == 1:
                print(Fore.GREEN + "Rolling a d%i... " % die[0] + str(random.randint(1, die[0])), Style.RESET_ALL)
                die_roller()
            else:
                result = 0
                for y in range (0, die[0]):
                    result = result + random.randint(1, die[1])
                if '+' in die_input:
                    result = result + die[2]
                    print(Fore.GREEN + "Rolling %id%i +%i... " % (die[0], die[1], die[2]) + str(result), Style.RESET_ALL)
                    die_roller()
                elif '-' in die_input:
                    result = result - die[2]
                    print(Fore.GREEN + "Rolling %id%i -%i... " % (die[0], die[1], die[2]) + str(result), Style.RESET_ALL)
                    die_roller()
                else:
                    print(Fore.GREEN + "Rolling %id%i... " % (die[0], die[1]) + str(result), Style.RESET_ALL)
                    die_roller()
        except IndexError:
            print(Fore.RED + "Invalid input. Type q to exit.", Style.RESET_ALL)
            die_roller()
