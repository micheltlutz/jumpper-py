# This code defines a class Em that inherits from the class TypographyElementBase
# It overrides the tag property of the parent class with the value "em"

class Em(TypographyElementBase):
    def __init__(self, text):
        self.text = text

    @property
    def tag(self):
        return "em"