# Ignore import Foundation

class ContainerElementBase:
    def __init__(self):
        pass

class Html(ContainerElementBase):
    def __init__(self):
        super().__init__()

    # Override tag element. Default is `html`
    @property
    def tag(self):
        return "html"