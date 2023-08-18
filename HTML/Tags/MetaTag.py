# Ignore import Foundation

class Meta(GenericElement):
    def __init__(self, *attributes):
        super().__init__(*attributes)
        
    @property
    def tag(self):
        return "meta"