# Ignore import Foundation

"""
Form tag element class

### Usage Example: ###
    form = Form((("method"),("POST")))
    fieldset = Fieldset()

    labelName = Label("Name")
    labelName.addAttribute(("for", "nameField"))
    fieldset.add(labelName)

    inputName = InputText("", id: "nameField", placeholder: "Name")
    fieldset.add(inputName)

    labelAge = Label("Age Range")
    labelAge.addAttribute(("for", "ageRangeField"))
    fieldset.add(labelAge)

    form.add(fieldset)
"""
class Form(GenericElement):
    # Override tag element for element. Default is `form`
    @property
    def tag(self):
        return "form"

    # Override container element defaults is `true`
    @property
    def container(self):
        return True

    # This method append a new element in objects list
    def add(self, element: GenericElement):
        self.objects.append(element)