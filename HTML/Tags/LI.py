# MIT License
#
# Copyright (c) 2020 micheltlutz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Class for list item
class LI(GenericElement):
    # Override tag element for input elements. Default is `li`
    @property
    def tag(self):
        return "li"
    
    # Override container element for table row elements defaults is `true`
    @property
    def container(self):
        return True
    
    # Initialization with Generic Type
    # - Parameter element: Generic Type `ElementProtocol` or `String`
    def __init__(self, element):
        super().__init__()
        if isinstance(element, str):
            text = FactoryElements.textWith(element)
            self.objects.append(text)
        elif isinstance(element, ElementProtocol):
            self.objects.append(element)