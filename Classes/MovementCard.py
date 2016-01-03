class MovementCard:
    Player = None
    IsPlaced = False
    MovementValue = 0

    def __init__(self, player):
        self.Player = player

    def is_placed(self):
        return self.MovementValue != 0

    def get_value(self):
        return self.MovementValue

    def give_coin(self):
        self.Player.give_coin()
