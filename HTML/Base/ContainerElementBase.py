# Define a base class to containered tag elements
class ContainerElementBase(GenericElement):
    # Override container element defaults is `true`
    @property
    def container(self):
        return True
    
    # This method append a new element in objects list
    # Parameter element: Generic Type `ElementProtocol` or `String`
    def add(self, element):
        if isinstance(element, str):
            text = FactoryElements.textWith(textElement)
            self.objects.append(text)
        else:
            genericElement = element
            if isinstance(genericElement, ElementProtocol):
                self.objects.append(genericElement)