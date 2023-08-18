# Python equivalent of the above Swift code

class ContainerElementBase:
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

class Title(ContainerElementBase):
    def __init__(self, text):
        super().__init__()
        self.add(text)

    @property
    def tag(self):
        return "title"

"""
title tag element class

### Usage Example: ###
pageTitle = Title("This is Page.")
"""