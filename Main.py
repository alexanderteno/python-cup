"""

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

"""
from Classes.Board import Board

board = Board()

board.init_camels()

spaces = board.get_spaces()

for i in range(3):
    print '----- SPACE ', i + 1, '-----'
    spaces[i].get_camel()
