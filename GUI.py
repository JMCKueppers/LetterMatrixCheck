# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LetterMatrixCheck.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelMatrix = QtWidgets.QLabel(self.centralwidget)
        self.labelMatrix.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.labelMatrix.setObjectName("labelMatrix")
        self.inputFieldMatrix = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputFieldMatrix.setGeometry(QtCore.QRect(20, 60, 321, 321))
        self.inputFieldMatrix.setObjectName("inputFieldMatrix")
        self.inputFieldKeyword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFieldKeyword.setGeometry(QtCore.QRect(390, 60, 211, 23))
        self.inputFieldKeyword.setObjectName("inputFieldKeyword")
        self.labelKeyword = QtWidgets.QLabel(self.centralwidget)
        self.labelKeyword.setGeometry(QtCore.QRect(390, 30, 91, 16))
        self.labelKeyword.setObjectName("labelKeyword")
        self.buttonCheck = QtWidgets.QToolButton(self.centralwidget)
        self.buttonCheck.setGeometry(QtCore.QRect(390, 110, 121, 22))
        self.buttonCheck.setObjectName("buttonCheck")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Letter Matrix Check"))
        self.labelMatrix.setText(_translate("MainWindow", "Buchstabenmatrix:"))
        self.labelKeyword.setText(_translate("MainWindow", "Suchwort:"))
        self.buttonCheck.setText(_translate("MainWindow", "Überprüfe Matrix"))
