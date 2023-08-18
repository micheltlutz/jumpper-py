# This code is defining a class named Strong that inherits from another class named TypographyElementBase
# The class overrides a property named tag with the value "strong"

class Strong(TypographyElementBase):
    def __init__(self, text):
        super().__init__(text)
    
    @property
    def tag(self):
        return "strong"