# This is a Python code that does the same thing as the swift code above

class TypographyElementBase:
    pass

class Small(TypographyElementBase):
    def __init__(self, text):
        self.text = text
        
    @property
    def tag(self):
        return "small"