# This is a Base class for Table Row Elements
class TableRowBase:
    # Override container element for table row elements defaults is `true`
    @property
    def container(self):
        return True

    # This method append a new element in objects list
    # - Parameter element: `ElementProtocol`
    def add(self, element):
        objects.append(element)