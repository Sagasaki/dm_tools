# Dice roller class #
# Functions to allow for random die rolls #

import random
import re


class Dice:
    @staticmethod
    def basic_roll(die_size):
        """ Engine that takes die type and returns the rolled value """
        result = random.randint(1, die_size)
        return result

    def custom_roll(self, multiple, die, modifier, modification):
        """ Allows for rolling die of the format 3d6+5 """
        result = multiple * self.basic_roll(die)
        if modifier == '+':
            result = result + modification
        elif modifier == '-':
            result = result - modification
        else:
            pass
        return result


class DiceInterface(Dice):
    def dice_prompt(self):
        die_input = input("Specify die roll in format '2d6(+/-)3': ")
        die = [i for i in re.findall('\\d+', die_input)]
        if die_input == 'q':
            exit()
        else:
            try:
                if len(die) == 1:
                    print("Rolling a d{}... {}".format(die[0], super().basic_roll(int(die[0]))))
                    self.dice_prompt()
                else:
                    result = 0
                    for y in range(0, int(die[0])):
                        result = result + super().basic_roll(int(die[1]))
                    if '+' in die_input:
                        result = result + int(die[2])
                        print("Rolling {}d{} +{}... {}".format(die[0], die[1], die[2], result))
                    elif '-' in die_input:
                        result = result - int(die[2])
                        print("Rolling {}d{} -{}... {}".format(die[0], die[1], die[2], result))
                    else:
                        print("Rolling {}d{}... {}".format(die[0], die[1], result))
            except IndexError:
                print("Invalid input. Type q to exit.")
                pass

    def interface(self):
        while True:
            self.dice_prompt()
