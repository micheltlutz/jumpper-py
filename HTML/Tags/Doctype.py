# Ignore import Foundation

# DOCTYPE tag element class
class Doctype:
    def __init__(self):
        self.tag = "<!DOCTYPE html>"

    def getString(self):
        return self.tag

    def generate(self):
        print(self.tag)