# Ignore import Foundation
# Class for description list item
class DT(LI):
    # Override tag element for input elements. Default is `dt`
    @property
    def tag(self):
        return "dt"