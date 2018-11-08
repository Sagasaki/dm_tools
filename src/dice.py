##  Dice roller  ##

import random


class Dice():
#    def __init__(self):


    def roll(self, max):
        result = random.randint(1, max)
        return result
