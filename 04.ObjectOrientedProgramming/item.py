# Take the inventory assignment and redo it as an object oriented programming project.
# Use a class for each inventory item and place those into a list.
# Import that into another python file and make sure your program functions the same
# as your previous assignment or better.

class Item:
    def __init__(self, name, quantity, description):
        self.name = name
        self.qty = quantity
        self.desc = description
