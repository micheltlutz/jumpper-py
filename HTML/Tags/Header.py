# Ignore import Foundation

"""
    header tag element class

    ### Usage Example: ###
    ```
    header = Header()
    header.add(/* Any Element*/)
    ```
"""
class Header(ContainerElementBase):
    # Override tag element. Default is `header`
    @property
    def tag(self):
        return "header"