class Button(TypographyElementBase):
    def __init__(self, content):
        super().__init__(content)

    @property
    def tag(self):
        return "button"