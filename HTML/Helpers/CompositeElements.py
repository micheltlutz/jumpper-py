# Ignore import Foundation
# Composite elements allows you to group elements without having to put an html container as the element root
# Usage
# ```python
# composite = CompositeElements()
# composite.add("Hello, World!")
# composite.add(Label("My Label"))
# ```
class CompositeElements:
    def __init__(self):
        self.objects = []

    # This method append a new element in objects list
    # - Parameter element: Generic Type `ElementProtocol` or `String`
    def add(self, element):
        if isinstance(element, str):
            text = FactoryElements.textWith(element)
            self.objects.append(text)
        elif isinstance(element, ElementProtocol):
            self.objects.append(element)

    # This method return tag and all elements
    # - Returns: `String` tag and all elements
    def getString(self):
        code = ""
        if len(self.objects) > 0:
            for obj in self.objects:
                code += obj.getString()
        return code

    # This method print tag and all elements
    def generate(self):
        if len(self.objects) > 0:
            for obj in self.objects:
                obj.generate()