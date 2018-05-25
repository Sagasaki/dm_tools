## Python class to contain a character's stats ##

"""Doc string"""

import pickle


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


char_list = []

# read in previously created characters
try:
    with open("characters.dat", 'rb') as file:
        char_list = pickle.load(file)
except (FileNotFoundError):
    pass

char = Character.create()
char_list.append(char)

for char in char_list:
    char.summary()

# save character list to file
with open("characters.dat", "wb+") as file:
    pickle.dump(char_list, file)
