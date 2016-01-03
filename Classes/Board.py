import random

from Camel import Camel
from TakeBetCard import TakeBetCard
from Space import Space
from Dice import Dice


class Board:
    Spaces = []
    FirstPlaceBets = []
    LastPlaceBets = []
    Camels = []
    TakeBetCards = []
    ProgressCards = range(5)
    Dice = []

    def __init__(self, size):
        for j in range(size):
            self.Spaces.append(Space())

    def get_camel_by_color(self, color_id):
        for camel in self.Camels:
            print camel.get_color()
            if camel.get_color_id() == color_id:
                return camel
        return Camel(-1, -1)

    def get_spaces(self):
        return self.Spaces

    def replace_take_bet_cards(self):
        self.TakeBetCards = []
        for j in range(5):
            self.TakeBetCards.append([])
            self.TakeBetCards[j].append(TakeBetCard(j, 5))
            self.TakeBetCards[j].append(TakeBetCard(j, 3))
            self.TakeBetCards[j].append(TakeBetCard(j, 2))

        return self.TakeBetCards

    def has_dice(self):
        return len(self.Dice) > 0

    def init_camels(self):
        camel_list = range(5)
        for j in range(5):
            index = random.randint(0, (len(camel_list) - 1))
            position = random.randint(0, 2)
            space = self.Spaces[position]
            occupying_camel = space.get_camel()
            new_camel = Camel(camel_list[index], position)
            if occupying_camel is None:
                self.Camels.append(new_camel)
                space.set_camel(new_camel)
            else:
                occupying_camel.set_camel(new_camel)

            del camel_list[index]

    def init_dice(self):
        for j in range(4):
            self.Dice.append(Dice(j))

    def progress_roll(self):
        x = random.randint(0, len(self.Dice) - 1)
        dice = self.Dice[x]
        target_color = dice.get_color_id()
        print '-- <DICE ROLL> --'
        print dice.get_color(), dice.get_value()
        print '-- </DICE ROLL> --'
        value = dice.get_value()
        self.Dice.remove(dice)
        camel = self.get_camel_by_color(target_color)
        print camel.get_color()
        if camel.get_color() != -1:
            camel.move(self.Spaces, value)

    def get_camels(self):
        return self.Camels
