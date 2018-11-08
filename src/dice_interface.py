from dice import Dice


class DiceInterface(Dice):
#    __init__(self):


    def dice_prompt(self):
        x = Dice()
        result = x.custom_roll(1, 20, '-', 5)
        print(result)


    def interface(self):
        self.dice_prompt()


x = DiceInterface()
x.interface()
