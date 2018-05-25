## Python class to contain a character's stats ##

"""Doc string"""

import pickle
import os

char_list = []



class Character:
    """Docstring"""

    def __init__(self, name, race, cls):
        self.name = name
        self.race = race
        self.cls = cls

    @classmethod
    def create(instance):
        return instance(
            input('Name: '),
            input('Race: '),
            input('Class: '))

    def update_class(self):
        self.cls = input('New class: ')

    def summary(self):
        print(self.name + " the " + self.race + " " + self.cls)



def write_out():
    global char_list
    with open("characters.dat", "wb") as file:
        pickle.dump(char_list, file)


def char_manager():

    global char_list

    # read in previously created characters
    try:
        with open("characters.dat", 'rb') as file:
            char_list = pickle.load(file)
    except (FileNotFoundError, EOFError):
        os.system('touch characters.dat')

    print("What would you like to do?")
    print("""Press q to exit.
    1. List all characters
    2. Create new character
    3. Print detailed character information
    4. Edit character
    5. Delete character
    """)
    selection = input()
    os.system('clear')

    if selection == '1':
        print('\nComplete character list:')
        for char in char_list:
            char.summary()
        print('\n')
        char_manager()

    elif selection == '2':
        char = Character.create()
        char_list.append(char)
        write_out()
        char_manager()

    elif selection == '3':
        name = input('\nType character name: ')
        for char in char_list:
            if char.name == name:
                char.summary()
            else:
                print("No character with this name")
        print('\n')
        char_manager()

    elif selection == '4':
        name = input('Type character name: ')
        for char in char_list:
            if char.name == name:
                char.update_class()
                write_out()
            else:
                print("No character with this name")
        char_manager()

    elif selection =='5':
        name = input('Type character name: ')
        for char in char_list:
            if char.name == name:
                sel = input("Are you certain you wish to delete this character? Deletions are permanant. Type Y to continue.")
                if sel == 'Y':
                    char_list.remove(char)
                    write_out()
                    print("Character " + name + " has been deleted.")
                else:
                    print("Character not deleted.")
            else:
                print("No character with this name")
        char_manager()


    elif selection == 'q':
        pass

    else:
        print("Invalid selection")
        char_manager()
