# This code is defining a class called "Main" which is a subclass of "ContainerElementBase"
# It overrides the tag property of the superclass and sets it to "main"

class Main(ContainerElementBase):
    # Override tag element for element. Default is `blockquote`
    @property
    def tag(self):
        return "main"