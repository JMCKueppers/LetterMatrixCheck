from Letter import *

class LetterMatrix:
    def __init__(self, inputMatrix):
        self.inputRows = inputMatrix.splitlines()
        self.rowLength = len(self.inputRows[0])
        self.columnLength = len(self.inputRows)
        self.rowIndices = range(self.columnLength)
        self.columnIndices = range(self.rowLength)
        self.matrix = [[Letter(self.inputRows[row][column], row, column) for column in self.columnIndices] for row in self.rowIndices]

    def getNumberOfInputRows(self):
        return len(self.inputRows)

    def correctInput(self):
        for row in self.inputRows:
            if len(row) != self.rowLength:
                return False
        return True

    def getSymbol(self, row, column):
        return self.inputRows[row][column]

    def getLetter(self, row, column):
        return self.matrix[row][column]

    def getNeighbours(self, row, column):
        neighbours = []
        if column-1 in self.columnIndices:
            neighbours.append(self.getLetter(row, column-1))
        if column+1 in self.columnIndices:
            neighbours.append(self.getLetter(row, column+1))
        if row-1 in self.rowIndices:
            neighbours.append(self.getLetter(row-1, column))
        if row+1 in self.rowIndices:
            neighbours.append(self.getLetter(row+1, column))
        return neighbours
