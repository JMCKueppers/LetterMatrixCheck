class Letter:
    def __init__(self, inputLetter, inputRow, inputColumn):
        self.letter = inputLetter
        self.row = inputRow
        self.column = inputColumn

    def __eq__(self, other):
        return (self.letter == other.letter and self.row == other.row and self.column == other.column)

    def getLetter(self):
        return self.letter

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column