# Python equivalent of the given Swift code

"""
MIT License

Copyright (c) 2020 micheltlutz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class Fieldset:
    """
    Fieldset tag element class

    Usage Example:
    fieldset = Fieldset()

    labelName = Label("Name")
    labelName.addAttribute(("for", "nameField"))
    fieldset.add(labelName)

    inputName = InputText("", id="nameField", placeholder="Name")
    fieldset.add(inputName)

    labelAge = Label("Age Range")
    labelAge.addAttribute(("for", "ageRangeField"))
    fieldset.add(labelAge)
    """

    def __init__(self):
        self.tag = "fieldset"

        # container element defaults is True
        self.container = True

        # objects list to hold appended elements
        self.objects = []

    def add(self, element):
        """
        This method appends a new element to objects list

        Parameters:
        element: ElementProtocol
        """
        self.objects.append(element)