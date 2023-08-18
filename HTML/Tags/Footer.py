# Ignore import Foundation

# Footer tag element class
class Footer(ContainerElementBase):
    # Override tag element. Default is `footer`
    def tag(self):
        return "footer"