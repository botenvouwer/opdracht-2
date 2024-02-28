class Header:

    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype

    def __str__(self):
        return f"{self.name} {self.datatype}"
