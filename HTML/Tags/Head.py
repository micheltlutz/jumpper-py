# Ignoring import Foundation as it is not relevant for Python

class Head(ContainerElementBase):
    # Override tag element for element. Default is `head`
    @property
    def tag(self):
        return "head"