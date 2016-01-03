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
import os
from Classes.Board import Board

board = Board(16)

board.init_camels()

spaces = board.get_spaces()

for i in range(16):
    print '----- SPACE ', i + 1, '-----'
    spaces[i].get_camel()

while True:
    print(' ----- NEW COMMAND ------')
    user_input = raw_input('Command:')
    if user_input.lower() == 'exit':
        break
    if not board.has_dice():
        board.init_dice()
    board.progress_roll()  # TODO: FIX THIS <--- FOR SOME REASON IT ISN'T GETTING THE CORRECT CAMEL
    os.system('cls')
    for i in range(16):
        print '----- SPACE ', i + 1, '-----'
        spaces[i].get_camel()
