##
## Dungeon Master's Digital Tool Set
## Copyright 2018 Jared C. Allen
##

"""
DM's Tools is a suite of useful tools to help a DM prepare for and run
a Dungeons and Dragons (5e) session.

This program should be able to:
 ->Create and edit player character's complete character sheet
 ->Manage encounters, including enemy HP, player HP, and track initiative
 ->Easy dice rolls for any situation, including rolling each char. stat
 ->Mapping tool for simple creation and tracking of dungeon adventures

The dm_tools.py module is the MAIN file for the DM's Tools program.
"""

import os
from dice.dice import die_roller
from colorama import Fore, Style

def main():
    os.system('clear')
    print(Fore.GREEN + """\nDungeon Master's Digital Tool Set
    Copyright 2018 Jared C. Allen\n""", Style.RESET_ALL)

    print(Fore.RED + """Please choose from the following options:
    1. D&D Dice Roller\n    """ + Style.DIM +
    """2. Player Character Manager
    3. Dungeon Map Editor
    4. Encounter Manager
    5. D&D Session View
    q. Quit""", Style.RESET_ALL)

    menu_opt = input()

    if menu_opt == '1':
        print(Fore.RED + "\nD&D Dice Roller. Type q to exit.\n", Style.RESET_ALL)
        die_roller()

    elif menu_opt == 'q':
        print("\nThank you for using the Dungeon Master's Digital Tool Set. Goodbye!\n")
        exit()

    else:
        main()

while True:
    main()
