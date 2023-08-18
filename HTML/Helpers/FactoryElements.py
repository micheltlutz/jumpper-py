class FactoryElements:
    # This method create a `Text` element to user when element T String is passed on add method
    # - Parameter text: `String` to create `Text` element
    # - Returns: `Text` Element with string passed
    @staticmethod
    def textWith(text):
        return Text(text)