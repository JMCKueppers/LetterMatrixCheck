from unittest import TestCase
from LetterMatrix import *


class TestLetter(TestCase):
    def setUp(self):
        self.letter = Letter('A', 1, 2)

    def test_getLetter(self):
        self.assertEqual(self.letter.getLetter(), 'A')

    def test_getRow(self):
        self.assertEqual(self.letter.getRow(), 1)

    def test_getColumn(self):
        self.assertEqual(self.letter.getColumn(), 2)

    def test_equal(self):
        letter2 = Letter('A', 1, 2)
        self.assertEqual(self.letter, letter2)


class TestLetterMatrix(TestCase):
    def setUp(self):
        self.input = 'abc\ndef\nghi'
        self.matrix = LetterMatrix(self.input)

    def test_split(self):
        self.assertEqual(self.matrix.inputRows, ['abc', 'def', 'ghi'])

    def test_rowLength(self):
        self.assertEqual(self.matrix.rowLength,3)

    def test_columnLength(self):
        self.assertEqual(self.matrix.columnLength, 3)

    def test_correctInputTrue(self):
        self.assertTrue(self.matrix.correctInput())

    def test_correctInputTrueNonQuadratic(self):
        input = 'abc\ndef\nghi\njkl'
        matrix = LetterMatrix(input)
        self.assertTrue(matrix.correctInput())

    def test_correctInputFalse(self):
        input = 'abc\ndefg\nhij'
        matrix = LetterMatrix(input)
        self.assertFalse(matrix.correctInput())

    def test_getSymbol(self):
        self.assertEqual(self.matrix.getSymbol(1, 1), 'e')

    def test_getNeigboursCenter(self):
        letter = Letter('e', 1, 1)
        expectedNeighbours = [Letter('d', 1, 0), Letter('f', 1, 2), Letter('b', 0, 1), Letter('h', 2, 1)]
        self.assertEqual(self.matrix.getNeighbours(letter), expectedNeighbours)

    def test_getNeighboursEdge(self):
        letter = Letter('a', 0, 0)
        expectedNeighbours = [Letter('b', 0, 1), Letter('d', 1, 0)]
        self.assertEqual(self.matrix.getNeighbours(letter), expectedNeighbours)

    def test_getNeighboursEdge2(self):
        letter = Letter('i', 2, 2)
        expectedNeighbours = [Letter('h', 2, 1), Letter('f', 1, 2)]
        self.assertEqual(self.matrix.getNeighbours(letter), expectedNeighbours)

    def test_wordAppearances(self):
        input = 'Katze'
        matrix = LetterMatrix(input)
        initialLetter = matrix.getLetter(0, 0)
        word = 'Katze'
        self.assertEqual(matrix.wordAppearances(initialLetter, word), 1)

    def test_wordAppearances2(self):
        input = 'Katze\naqrxy\ntqrxy\nzqrxy\neqrxy'
        matrix = LetterMatrix(input)
        initialLetter = matrix.getLetter(0, 0)
        word = 'Katze'
        self.assertEqual(matrix.wordAppearances(initialLetter, word), 2)

    def test_totalWordAppearances(self):
        input = 'Katze\nKatze\nKatze'
        matrix = LetterMatrix(input)
        word = 'Katze'
        self.assertEqual(matrix.totalWordAppearances(word), 3)

    def test_totalWordAppearances2(self):
        input = 'KKK\naaa\nttt\nzzz\neee'
        matrix = LetterMatrix(input)
        word = 'Katze'
        self.assertEqual(matrix.totalWordAppearances(word), 3)