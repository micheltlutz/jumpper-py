class TypographyElementBase(GenericElement):
    def __init__(self, element):
        super().__init__()
        self.add(element)
    
    @property
    def container(self):
        return True
    
    def add(self, element):
        if isinstance(element, str):
            text = FactoryElements.textWith(element)
            self.objects.append(text)
        elif isinstance(element, ElementProtocol):
            self.objects.append(element)