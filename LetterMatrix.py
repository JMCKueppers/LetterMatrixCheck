class LetterMatrix:
    def __init__(self, inputMatrix):
        self.inputRows = inputMatrix.splitlines()
        self.rowLength = len(self.inputRows[0])
        self.columnLength = len(self.inputRows)

    def getNumberOfInputRows(self):
        return len(self.inputRows)

    def correctInput(self):
        for row in self.inputRows:
            if len(row) != self.rowLength:
                return False
        return True
