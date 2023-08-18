# This code defines a class P that inherits from TypographyElementBase
# It sets the tag property of TypographyElementBase to "p"

class TypographyElementBase:
    def __init__(self):
        pass

class P(TypographyElementBase):
    @property
    def tag(self):
        return "p"