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
        if self.ui.boxCaseSensitivity.isChecked():
            self.inputMatrix = self.ui.inputFieldMatrix.toPlainText()
            self.inputWord = self.ui.inputFieldKeyword.text()
        else:
            self.inputMatrix = self.ui.inputFieldMatrix.toPlainText().upper()
            self.inputWord = self.ui.inputFieldKeyword.text().upper()
        myMatrix = LetterMatrix(self.inputMatrix)
        if myMatrix.correctInput():
            numberOfWordAppearances = str(myMatrix.totalWordAppearances(self.inputWord))
            self.ui.labelOutput.setText("Das Wort wurde "+numberOfWordAppearances+" mal gefunden")
        else:
            self.ui.labelOutput.setText("Ungültige Eingabe")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    sys.exit(app.exec_())
