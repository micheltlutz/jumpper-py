# Define a SelectOptionsType as a list of dictionaries with string keys and custom description values
SelectOptionsType = List[Dict[str, Any]]

class Select(GenericElement):
    # Override the tag element for option, default is 'option'
    @property
    def tag(self):
        return 'select'
    
    # Override the container element for table row elements, default is True
    @property
    def container(self):
        return True
    
    # List with array of SelectOptionsType, default is an empty list
    def __init__(self, options: SelectOptionsType = [], *attributes: AttributeType):
        super().__init__(*attributes)
        self.options = options
        self.makeOptions()
    
    # This method iterates over the list of options and creates the option element for each of the items
    def makeOptions(self):
        for optionDic in self.options:
            for key, value in optionDic.items():
                option = Option(key, text=value)
                self.objects.append(option)