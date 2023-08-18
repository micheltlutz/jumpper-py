# Tbody tag element class
class TBody(TableRowBase):
    
    # Override tag element for element. Default is `tbody`
    @property
    def tag(self):
        return "tbody"