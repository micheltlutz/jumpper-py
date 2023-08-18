# Python equivalent of LinkStylesheet class in Swift

class LinkStylesheet(Link):
    """
    Link stylesheet tag element class

    Usage Example:
    linkCssTag = LinkStylesheet("/styles/milligram.min.css")
    """

    def __init__(self, href: str):
        super().__init__(href)
        self.addAttribute(("rel", "stylesheet"))