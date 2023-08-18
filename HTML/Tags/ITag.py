# This code defines a class I, which inherits from ContainerElementBase.
# It overrides the tag property to always return "i".
# This class is used to represent an HTML <i> tag with an optional class attribute.

class I(ContainerElementBase):
    # Override tag element for element. Default is `i`
    @property
    def tag(self):
        return "i"