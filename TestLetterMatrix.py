from unittest import TestCase
from LetterMatrix import *


class TestLetterMatrix(TestCase):
    def setUp(self):
        self.input = 'abc\ndef'
        self.matrix = LetterMatrix(self.input)

    def test_split(self):
        self.assertEqual(self.matrix.inputRows, ['abc', 'def'])

    def test_rowLength(self):
        self.assertEqual(self.matrix.rowLength,3)

    def test_columnLength(self):
        self.assertEqual(self.matrix.columnLength, 2)

    def test_correctInputTrue(self):
        self.assertTrue(self.matrix.correctInput())

    def test_correctInputFalse(self):
        input = 'abc\ndefg'
        matrix = LetterMatrix(input)
        self.assertFalse(matrix.correctInput())
