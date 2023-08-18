class GenericElement:
    def __init__(self, *attributes):
        self.attributes = list(attributes)
        self.tag = ""
        self.container = False
        self.formElement = False
        self.objects = []

    def addAttribute(self, attr):
        self.attributes.append(attr)

    def openTag(self):
        attr = Attribute(self.attributes)
        return f"<{self.tag}{attr.getString()}>"

    def closeTag(self):
        return f"</{self.tag}>"

    def getString(self):
        code = self.openTag()

        if len(self.objects) > 0:
            for obj in self.objects:
                code += obj.getString()

        if self.container:
            code += self.closeTag()

        return code

    def generate(self):
        print(self.openTag())
        if len(self.objects) > 0:
            for obj in self.objects:
                obj.generate()
        print(self.closeTag())