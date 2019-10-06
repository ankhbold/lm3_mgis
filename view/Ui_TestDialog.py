# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TestDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestDialog(object):
    def setupUi(self, TestDialog):
        TestDialog.setObjectName("TestDialog")
        TestDialog.resize(445, 504)
        self.test_button = QtWidgets.QPushButton(TestDialog)
        self.test_button.setGeometry(QtCore.QRect(310, 60, 75, 23))
        self.test_button.setObjectName("test_button")
        self.close_button = QtWidgets.QPushButton(TestDialog)
        self.close_button.setGeometry(QtCore.QRect(310, 460, 75, 23))
        self.close_button.setObjectName("close_button")

        self.retranslateUi(TestDialog)
        QtCore.QMetaObject.connectSlotsByName(TestDialog)

    def retranslateUi(self, TestDialog):
        _translate = QtCore.QCoreApplication.translate
        TestDialog.setWindowTitle(_translate("TestDialog", "Dialog"))
        self.test_button.setText(_translate("TestDialog", "TEST"))
        self.close_button.setText(_translate("TestDialog", "Close"))

