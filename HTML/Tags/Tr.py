# Python equivalent of the Swift code above
# Ignore import Foundation

# Tr tag element class
class Tr(TableRowBase):
    
    # Override tag element for element. Default is `tr`
    @property
    def tag(self):
        return "tr"