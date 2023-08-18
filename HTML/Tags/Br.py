# This code defines a class for the HTML <br> tag element
class Br:
    # This is a subclass of a GenericElement class
    class GenericElement:
        pass

    # This overrides the tag variable of the parent class to always return "br"
    @property
    def tag(self):
        return "br"