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
"""

import os
from dice import DiceInterface

dice = DiceInterface()


def main():
    os.system('clear')
    print("""\nDungeon Master's Digital Tool Set\nCopyright 2018 Jared C. Allen\n""")

    print("""Please choose from the following options:
    1. D&D Dice Roller
    2. Player Character Manager
    3. Dungeon Map Editor
    4. Encounter Manager
    5. D&D Session View
    q. Quit""")

    menu_opt = input()

    if menu_opt == '1':
        print("\nD&D Dice Roller. Type q to exit.\n")
        dice.interface()

    elif menu_opt == 'q':
        print("\nThank you for using the Dungeon Master's Digital Tool Set. Goodbye!\n")
        exit()

    else:
        main()

while True:
    main()

