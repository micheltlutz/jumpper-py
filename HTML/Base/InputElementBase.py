class InputElementBase(GenericElement):
    def __init__(self, value, type):
        super().__init__()
        self.addAttribute(("value", value))
        self.addAttribute(("type", type))

    @property
    def tag(self):
        return "input"

    @property
    def formElement(self):
        return True