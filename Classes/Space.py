FORWARD = 'Forward'
BACKWARD = 'Backward'


class CardException(Exception):
    pass


class Space:
    MovementCard = None
    Camel = None

    def __init__(self):
        return

    def has_card(self):
        return self.MovementCard is not None

    def place_card(self, movement_card):
        if not self.has_card():
            self.MovementCard = movement_card
        else:
            raise CardException('Has MovementCard already.')  # TODO: Give localization

    def remove_card(self):
        self.MovementCard = None

    def get_card(self):
        return self.MovementCard

    def get_id(self):
        return id(self)

    def set_bottom_camel(self, new_camel):
        current_camel = self.Camel
        if current_camel is not None:
            current_camel.set_camel(new_camel)
        else:
            current_camel.immediate_break(new_camel)
            self.Camel = new_camel
            new_camel.set_camel(current_camel)


    def get_camel(self):
        if self.Camel is not None:
            print self.Camel.get_color(), ' -- >'
            return self.Camel.get_top_camel()
        else:
            print ('No Camel')
            return self.Camel

    def set_camel(self, camel):
        self.Camel = camel

    def camel_break(self, current_space):
        if self.Camel is not None:
            if self.Camel.get_space() == current_space:
                self.Camel.camel_break(current_space)
            else:
                self.Camel = None
