import random

from Camel import Camel
from LegOfRaceBettingCard import LegOfRaceBettingCard
from Space import Space


class Board:
    Spaces = []
    FirstPlaceBets = []
    LastPlaceBets = []
    Camels = []
    LegOfRaceBettingCards = []
    ProgressCards = range(5)

    def __init__(self):
        for j in range(16):
            self.Spaces.append(Space())

    def get_spaces(self):
        return self.Spaces

    def replace_leg_of_race_betting_cards(self):
        self.LegOfRaceBettingCards = []
        for j in range(5):
            self.LegOfRaceBettingCards.append([])
            self.LegOfRaceBettingCards[j].append(LegOfRaceBettingCard(j, 5))
            self.LegOfRaceBettingCards[j].append(LegOfRaceBettingCard(j, 3))
            self.LegOfRaceBettingCards[j].append(LegOfRaceBettingCard(j, 2))

        return self.LegOfRaceBettingCards

    def init_camels(self):
        camel_list = range(5)
        for j in range(5):
            index = random.randint(0, (len(camel_list) - 1))
            position = random.randint(0, 2)
            space = self.Spaces[position]
            occyping_camel = space.get_camel()
            new_camel = Camel(camel_list[index], position)
            if occyping_camel is None:
                self.Camels.append(new_camel)
                space.set_camel(new_camel)
            else:
                occyping_camel.set_camel(new_camel)

            del camel_list[index]

    def get_camels(self):
        return self.Camels