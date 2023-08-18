class Checkbox(InputElementBase):
    # Class define a input type checkbox
    
    # Usage Example:
    # Checkbox("confirmField", id: "confirmField")
    
    def __init__(self, name: str, id: str):
        super().__init__("", "checkbox")
        
        self.addAttribute(("name", name))
        
        if id:
            self.addAttribute(("id", id))