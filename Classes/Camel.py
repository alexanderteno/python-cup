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
