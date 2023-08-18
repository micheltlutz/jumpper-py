# Ignore import Foundation

"""
   Table html tag class element

    ### Usage Example: ###
    ````python
     table = Table()
     table.tableHeaders(titles=["Name", "Age", "Height", "Location"])
     #table.tableHeaders(titles=["Name", "Age", "Height", "Location"], aligns=["center", "left", "left", "left"]) # Align Headers

     table.addRow()
     table.addInRow("Arthurito Thompson")
     table.addInRow("52")
     table.addInRow("1,30")
     table.addInRow("Torresmo, RS")
     table.addRow()
     table.addInRow("Stephen Curry")
     table.addInRow("27")
     table.addInRow("1,91")
     table.addInRow("Akron, OH")
     table.addRow()
     table.addInRow("Klay Thompson")
     table.addInRow("25")
     table.addInRow("2,01")
     table.addInRow("Los Angeles, CA")
    ````
"""
class Table(GenericElement):
    def __init__(self):
        self.tbody = TBody() # Object with table body. tr, td: `TBody`
        self.thead = None # Object with table head. th, td: THead? is optional
        self.rows = [] # List of rows a array of `Tr`tag element

    @property
    def tag(self): # Override tag element for element. Default is `table`
        return "table"

    @property
    def container(self): # Override container element defaults is `True`
        return True

    def tableHeaders(self, titles: [str], aligns: [str] = None, class_: [str] = None): # This method append a new eow element in row objects list
        self.thead = THead()

        for index, title in enumerate(titles):
            th = Th()
            th.add(title)

            if aligns:
                align = aligns[index]
                th.addAttribute(("align", align))

            if class_:
                classItem = class_[index]
                th.addAttribute(("class", classItem))
            self.thead.add(th)

    def addRow(self, *attributes: AttributeType): # This method append a new eow element in row objects list
        tr = Tr(attributes)

        self.rows.append(tr)
        return tr

    def addInRow(self, element, *attributes: AttributeType): # This method append a new collumn element in row objects list
        td = Td(attributes)

        td.add(element)

        if not self.rows:
            raise Exception("‼️ [Wrong usage for addInRow] Use addRow first to create a new row")

        lastRow = self.rows[-1]
        lastRow.add(td)
        return td

    def getString(self): # Override method return tag and all elements
        code = self.openTag()
        if self.thead:
            code += self.thead.getString()

        for row in self.rows:
            self.tbody.add(row)

        code += self.tbody.getString()
        code += self.closeTag()
        return code

    def generate(self): # Override generate methot do print elements
        print(self.getString())