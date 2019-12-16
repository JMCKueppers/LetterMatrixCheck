import sys

from PyQt5.QtWidgets import *

from GUI import Ui_MainWindow
from LetterMatrix import *


class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inputMatrix = self.ui.inputFieldMatrix.toPlainText()
        self.inputWord = self.ui.inputFieldKeyword.text()
        self.ui.buttonCheck.clicked.connect(self.clickMethod)

    def clickMethod(self):
        self.inputMatrix = self.ui.inputFieldMatrix.toPlainText()
        self.inputWord = self.ui.inputFieldKeyword.text()
        print(self.inputMatrix)
        print(self.inputWord)
        myMatrix = LetterMatrix(self.inputMatrix)
        print(myMatrix.correctInput())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    sys.exit(app.exec_())
