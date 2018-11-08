from dice import Dice


class DiceInterface(Dice):
#    __init__(self):


    def dice_prompt(self):
        x = Dice()
        max_roll = int(input('Specify die size: '))
        roll = x.roll(max_roll)
        return roll


    def interface(self):
        self.dice_prompt()


x = DiceInterface()
print(x.interface())
