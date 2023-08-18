# Ignoring import Foundation

class Label(TypographyElementBase):
    # Override tag element for element. Default is `label`
    @property
    def tag(self):
        return "label"