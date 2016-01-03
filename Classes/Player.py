class Player:
    Wallet = 0
    Name = None
    PlaceBetCards = []
    TakeBetCards = []

    def __init__(self, name):
        self.Name = name

    def init_place_bet_cards(self):
        self.PlaceBetCards = range(5)

    def give_coin(self, amount=1):
        self.Wallet += amount
