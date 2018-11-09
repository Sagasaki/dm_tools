## Dice roller class ##
## Functions to allow for random die rolls ##

import random
import re


class Dice():
    def basic_roll(self, max):
        """ Engine that takes die type and returns the rolled value """
        result = random.randint(1, max)
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
        die = [int(x) for x in re.findall('\\d+', die_input)]
        if die_input == 'q':
            exit()
        else:
            try:
                if len(die) == 1:
                    print("Rolling a d%i... " % die[0] + self.basic_roll(die[0]))
                    dice_prompt()
                else:
                    result = 0
                    for y in range (0, die[0]):
                        result = result + self.basic_roll(die[1])
                    if '+' in die_input:
                        result = result + die[2]
                        print("Rolling %id%i +%i... " % (die[0], die[1], die[2]) + str(result))
                    elif '-' in die_input:
                        result = result - die[2]
                        print("Rolling %id%i -%i... " % (die[0], die[1], die[2]) + str(result))
                    else:
                        print("Rolling %id%i... " % (die[0], die[1]) + str(result))
            except IndexError:
                print("Invalid input. Type q to exit.")
                pass
    

    def interface(self):
        while True:
            self.dice_prompt()
