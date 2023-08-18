# This is a python implementation of the above Swift code with comments. 

# A tag element class
# Usage Example:
# link = Link(("href","https://micheltlutz.me"), ("target","_blank"))
# link.add("Developed by Michel Lutz - micheltlutz.me 🚀")
class A(ContainerElementBase):
    # Override tag element for element. Default is `a`
    @property
    def tag(self):
        return "a"