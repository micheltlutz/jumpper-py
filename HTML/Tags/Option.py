#This class define a option select element
class Option(GenericElement):
    
    #Override tag element for option. Default is `option`
    @property
    def tag(self):
        return "option"
    
    #Override container element for table row elements defaults is `true`
    @property
    def container(self):
        return True

    # MARK: - Initialization
    
    #Default initializer option element
    def __init__(self, value: CustomStringConvertible, text: CustomStringConvertible):
        super().__init__()
        self.addAttribute(("value", value.description))
        self.objects.append(Text(text.description))