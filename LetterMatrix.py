class LetterMatrix:
    def __init__(self, inputMatrix):
        self.inputRows = inputMatrix.splitlines()

    def getNumberOfInputRows(self):
        return len(self.inputRows)

    def correctInput(self):
        rowLength = len(self.inputRows[0])
        for row in self.inputRows:
            if len(row) != rowLength:
                return False
        return True

