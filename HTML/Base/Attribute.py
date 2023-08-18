/// AttributeType is a Tuple (String, String?)
AttributeType = Tuple[str, Optional[str]]

## This class is responsible for managing attributes of HTML elements
class Attribute:
    ## Contains a array of AttributeType. Default is `[]`
    def __init__(self, attributes: List[AttributeType] = []):
        self.attributes = attributes

    ## This method add a new single attribute
    def add(self, attr: AttributeType):
        self.attributes.append(attr)

    ## This function return all attribures
    def getAll(self) -> List[AttributeType]:
        return self.attributes

    ## This method return a `String` with all attributes
    def getString(self) -> str:
        attrs = ""

        for attr, value in self.attributes:
            if value is not None:
                attrs += f" {attr}='{value}'"
            else:
                attrs += f" {attr}"

        return attrs

    ## This method print all attributes
    def generate(self):
        print(self.getString())