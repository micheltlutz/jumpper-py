# This code defines classes for HTML heading tags - H1, H2, H3, H4, H5, H6

# H1 tag element class
class H1(TypographyElementBase):
    # Override tag element for element. Default is `h1`
    @property
    def tag(self):
        return "h1"
    
# H2 tag element class
class H2(TypographyElementBase):
    # Override tag element for element. Default is `h2`
    @property
    def tag(self):
        return "h2"

# H3 tag element class
class H3(TypographyElementBase):
    # Override tag element for element. Default is `h3`
    @property
    def tag(self):
        return "h3"

# H4 tag element class
class H4(TypographyElementBase):
    # Override tag element for element. Default is `h4`
    @property
    def tag(self):
        return "h4"

# H5 tag element class
class H5(TypographyElementBase):
    # Override tag element for element. Default is `h5`
    @property
    def tag(self):
        return "h5"

# H6 tag element class
class H6(TypographyElementBase):
    # Override tag element for element. Default is `h6`
    @property
    def tag(self):
        return "h6"