# Ignore import Foundation

# Body tag element class
class Body(ContainerElementBase):
    # Override tag element. Default is `body`
    @property
    def tag(self):
        return "body"