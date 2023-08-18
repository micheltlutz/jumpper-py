# This class define a Textarea element
class Textarea(GenericElement):
    # Override tag element for option. Default is `textarea`
    @property
    def tag(self):
        return "textarea"
    
    # Override container element for table row elements defaults is `true`
    @property
    def container(self):
        return True
    
    # This method add a text in textarea element
    # - Parameters:
    #     - text: This is a text for select **text** `String`
    def add(self, text):
        self.objects.append(Text(text))