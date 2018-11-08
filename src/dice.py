## Dice roller class ##
## Functions to allow for random die rolls ##

import random


class Dice():
    def _roll(self, max):
        """ Engine that takes die type and returns the rolled value """
        result = random.randint(1, max)
        return result
        
        
    def custom_roll(self, multiple, die, modifier, modification):
        """ Allows for rolling die of the format 3d6+5 """
        result = multiple * self._roll(die)
        if modifier == '+':
            result = result + modification
        elif modifier == '-':
            result = result - modification
        else:
            pass
        return result
