# This code is a class in Swift for ordered lists. It inherits from another class named UL which is not shown here.
# The class is declared as a public final class named OL.
# It has an overridden computed property named tag which returns the string "ol".
# The import statement for Foundation is not required in Python.

class OL(UL):
    # Override tag element for input elements. Default is 'ol'
    @property
    def tag(self):
        return 'ol'