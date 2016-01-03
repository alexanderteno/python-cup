class TakeBetCard:
    CamelId = None
    FirstValue = None
    SecondValue = 1
    LowValue = -1

    def __init__(self, camel_id, first_value):
        self.CamelId = camel_id
        self.FirstValue = first_value

    def get_camel_id(self):
        return self.CamelId

    def get_first_value(self):
        return self.FirstValue
