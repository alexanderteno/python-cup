from Space import Space

COLORS = ['Blue', 'Green', 'Red', 'Yellow', 'White']


class Camel:
    ColorId = None
    SucceedingCamel = None
    BoardPosition = None
    Space = None

    def __init__(self, color_id, space):
        self.ColorId = color_id
        self.Space = space

    def get_space(self):
        return self.Space

    def get_color(self):
        return COLORS[self.ColorId]

    def get_color_id(self):
        return self.ColorId

    def set_camel(self, camel):
        if self.SucceedingCamel is None:
            self.SucceedingCamel = camel
        else:
            self.SucceedingCamel.set_camel(camel)

    def get_top_camel(self):
        if self.SucceedingCamel is None:
            return self
        else:
            print self.SucceedingCamel.get_color(), ' --> '
            return self.SucceedingCamel.get_top_camel()

    def set_space(self, space):
        self.Space = space
        if self.SucceedingCamel is not None:
            self.SucceedingCamel.set_space(space)

    def camel_break(self, current_space):
        if self.SucceedingCamel is not None:
            if self.SucceedingCamel.get_space() == current_space:
                self.SucceedingCamel.camel_break(current_space)
            else:
                self.SucceedingCamel = None

    def move(self, spaces, value):
        current_space = self.Space
        card_value = 0
        new_space = min(current_space + value, len(spaces) - 1)
        if spaces[new_space].__class__ == Space:
            if spaces[new_space].has_card():
                movement_card = spaces[new_space].get_card()
                card_value = movement_card.get_value()
                new_space = new_space + card_value

            new_space = min(new_space, len(spaces) - 1)

            self.Space = new_space
            if self.SucceedingCamel is not None:
                self.SucceedingCamel.set_space(new_space)

            # TODO: LINK CAMEL
            if card_value > 0:
                spaces[new_space].set_camel(self)
            elif card_value < 0:
                spaces[new_space].set_bottom_camel(self)

            spaces[current_space].camel_break(current_space)

        else:
            print ('I\'m angry at you.')

    def immediate_break(self, breaking_camel):
        if self.SucceedingCamel is not None:
            if self.SucceedingCamel == breaking_camel:
                self.SucceedingCamel = None
            else:
                self.SucceedingCamel.immediate_break(breaking_camel)
