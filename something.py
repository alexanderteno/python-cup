'''

GAME

        // BOARD
                // SPACES
                        // PROPS
                // CARDS
                        - PROGRESS
                        - BET <-- COLLECT
                        - BET --> PLACE
                // CAMELS
                // DICE
                // ENDING BETS
                        - FIRST PLACE
                        - LAST PLACE

        // PLAYERS
                // MONEY
                // BETTING CARDS
                // TAKEN BETS
                // PROGRESS CARDS
                // OBSTACLE TILES

        // MONEY

'''
import random

_forward = 'Forward'
_backward = 'Backward'

Colors = ['Blue', 'Green', 'Red', 'Yellow', 'White']

class Player:

        Id = None

        def __init__(self, id):
                Id = id

class Camel:

        Id = None
        SucceedingCamel = None
        BoardPosition = None
        Space = None

        def __init__(self, id, space):
                self.Id = id
                self.Space = space

        def getSpace(self):
                return self.Space

        def getColor(self):
                return Colors[self.Id]

        def setCamel(self, camel):
                if self.SucceedingCamel is None:
                        self.SucceedingCamel = camel
                else:
                        self.SucceedingCamel.setCamel(camel)

        def getTopCamel(self):
                if self.SucceedingCamel is None:
                        return self
                else:
                        print self.SucceedingCamel.getColor(), ' --> '
                        return self.SucceedingCamel.getTopCamel()

class Space:

        Forward = False
        Backward = False
        PlayerReward = None
        Id = None
        Camel = None

        def __init__(self, id):
                self.Id = id

        def hasCard(self):
                return self.playerReward is not None

        def placeCard(self, direction, player):
                if (not self.hasCard()):
                        if (direction == _forward):
                                forward = True
                        elif (direction == _backward):
                                backward = True
                        PlayerReward = player

        def removeCard(self):
                Forward = False
                Backward = False
                playerReward = None

        def getId(self):
                return self.Id

        def getCamel(self):
                if self.Camel is not None:
                        print self.Camel.getColor(), ' -- >'
                        return self.Camel.getTopCamel()
                else:
                        print ('No Camel')
                        return self.Camel

        def setCamel(self, camel):
                self.Camel = camel

class LegOfRaceBettingCard:

        CamelId = None
        FirstValue = None
        SecondValue = 1
        LowValue = -1

        def __init__(self, camelId, firstValue):
                self.CamelId = camelId
                self.FirstValue = firstValue

        def getCamelId(self):
                return self.CamelId

        def getFirstValue(self):
                return self.FirstValue

class Board:

        Spaces = []
        FirstPlaceBets = []
        LastPlaceBets = []
        Camels = []
        LegOfRaceBettingCards = []
        ProgressCards = range(5)

        def __init__(self):
                for i in range(16):
                        self.Spaces.append(Space(i))

        def getSpaces(self):
                return self.Spaces
        
        def replaceLegOfRaceBettingCards(self):
                self.LegOfRaceBettingCards = []
                for i in range(5):
                        self.LegOfRaceBettingCards.append([])
                        self.LegOfRaceBettingCards[i].append(LegOfRaceBettingCard(i, 5))
                        self.LegOfRaceBettingCards[i].append(LegOfRaceBettingCard(i, 3))
                        self.LegOfRaceBettingCards[i].append(LegOfRaceBettingCard(i, 2))

                return self.LegOfRaceBettingCards

        def initCamels(self):
                camelList = range(5)
                for i in range(5):
                        index = random.randint(0,(len(camelList) - 1))
                        position = random.randint(0,2)
                        space = self.Spaces[position]
                        occupyingCamel = space.getCamel()
                        newCamel = Camel(camelList[index], position)
                        if (occupyingCamel is None):
                                self.Camels.append(newCamel)
                                space.setCamel(newCamel)
                        else:
                                occupyingCamel.setCamel(newCamel)
                                
                        del camelList[index]

        def getCamels(self):
                return self.Camels
                        

board = Board()

board.initCamels()

spaces = board.getSpaces()

for i in range(3):

        print '----- SPACE ', i + 1, '-----'
        spaces[i].getCamel()
