# Ignore import Foundation

# Th tag element class
class Th(TableColumnBase):
    # Override tag element for element. Default is `th`
    @property
    def tag(self):
        return "th"