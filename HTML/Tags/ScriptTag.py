# This class define a Script element

class GenericElement:
    def __init__(self):
        self.tag = ''
        self.container = False

class Text:
    def __init__(self, text):
        self.text = text

class Script(GenericElement):
    def __init__(self):
        self.tag = 'script'

    def add(self, text):
        self.objects.append(Text(text))