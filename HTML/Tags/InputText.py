# This code defines a class for an input type text
# Usage example: InputText("value", id="nameField", placeholder="Name")

class InputText:
    # Default initializer for input text element
    def __init__(self, value: str, id: str = None, placeholder: str = None):
        super().__init__(value, type="text")
        if placeholder:
            self.addAttribute(("placeholder", placeholder))
        if id:
            self.addAttribute(("id", id))