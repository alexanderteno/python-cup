FORWARD = 'Forward'
BACKWARD = 'Backward'

class Space:
    Forward = False
    Backward = False
    RewardedPlayer = None
    Camel = None

    def __init__(self):
        return

    def has_card(self):
        return self.RewardedPlayer is not None

    def place_card(self, direction, player):
        if not self.has_card():
            if direction == FORWARD:
                self.Forward = True
            elif direction == BACKWARD:
                self.Backward = True
            self.RewardedPlayer = player

    def remove_card(self):
        self.Forward = False
        self.Backward = False
        self.RewardedPlayer = None

    def get_id(self):
        return id(self)

    def get_camel(self):
        if self.Camel is not None:
            print self.Camel.get_color(), ' -- >'
            return self.Camel.get_top_camel()
        else:
            print ('No Camel')
            return self.Camel

    def set_camel(self, camel):
        self.Camel = camel