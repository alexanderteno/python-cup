import random

COLORS = ['Blue', 'Green', 'Red', 'Yellow', 'White']


class Dice:
    ColorId = None

    def __init__(self, color_id):
        self.ColorId = color_id

    def get_color(self):
        return COLORS[self.ColorId]

    def get_color_id(self):
        return self.ColorId

    @staticmethod
    def get_value():
        return random.randint(1, 3)
