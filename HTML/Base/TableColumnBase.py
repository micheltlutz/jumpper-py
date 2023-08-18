class TableColumnBase:
    # This is a Base class for Table Column Elements
    def __init__(self):
        self.objects = []

    # Override container element for table row elements defaults is `True`
    @property
    def container(self):
        return True

    # This method append a new element in objects list
    # Parameter element: Generic Type `ElementProtocol` or `String`
    def add(self, element):
        if isinstance(element, str):
            text = FactoryElements.textWith(element)
            self.objects.append(text)
        elif isinstance(element, ElementProtocol):
            self.objects.append(element)