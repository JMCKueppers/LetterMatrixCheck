from Letter import *


class LetterMatrix:
    def __init__(self, inputMatrix):
        self.inputRows = inputMatrix.splitlines()
        self.rowLength = len(self.inputRows[0])
        self.columnLength = len(self.inputRows)
        self.rowIndices = range(self.columnLength)
        self.columnIndices = range(self.rowLength)
        if self.correctInput():
            self.matrix = [[Letter(self.inputRows[row][column], row, column) for column in self.columnIndices] for row in self.rowIndices]
        else:
            self.matrix = [[]]
            print('Incorrect Input')

    def getNumberOfInputRows(self):
        return len(self.inputRows)

    def correctInput(self):
        for row in self.inputRows:
            if len(row) != self.rowLength:
                return False
        return True

    def getSymbol(self, row, column):
        return self.matrix[row][column].getLetter()

    def getLetter(self, row, column):
        return self.matrix[row][column]

    def getNeighbours(self, letter):
        row = letter.getRow()
        column = letter.getColumn()
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

    def totalWordAppearances(self, word):
        totalWordCounter = 0
        for row in self.rowIndices:
            for column in self.columnIndices:
                initialLetter = self.getLetter(row,column)
                totalWordCounter += self.wordAppearances(initialLetter, word)
        return totalWordCounter

    def wordAppearances(self, initialLetter, word):
        wordCounter = 0
        neighbours = self.getNeighbours(initialLetter)
        if initialLetter.getLetter() == word[0]:
            if len(word) > 1:
                remainingWord = word[1:]
                for neighbour in neighbours:
                    wordCounter += self.wordAppearances(neighbour, remainingWord)
            if len(word) == 1:
                wordCounter += 1
                print('Hi')
        return wordCounter
