# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ManageParcelRecordsDialog.ui'
#
# Created: Thu Apr 23 13:55:11 2015
#      by: PyQt5 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ManageParcelRecordsDialog(object):
    def setupUi(self, ManageParcelRecordsDialog):
        ManageParcelRecordsDialog.setObjectName(_fromUtf8("ManageParcelRecordsDialog"))
        ManageParcelRecordsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ManageParcelRecordsDialog.setEnabled(True)
        ManageParcelRecordsDialog.resize(450, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManageParcelRecordsDialog.sizePolicy().hasHeightForWidth())
        ManageParcelRecordsDialog.setSizePolicy(sizePolicy)
        ManageParcelRecordsDialog.setMinimumSize(QtCore.QSize(450, 400))
        ManageParcelRecordsDialog.setMaximumSize(QtCore.QSize(450, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        ManageParcelRecordsDialog.setFont(font)
        ManageParcelRecordsDialog.setMouseTracking(False)
        ManageParcelRecordsDialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        ManageParcelRecordsDialog.setModal(False)
        self.addButton = QtGui.QPushButton(ManageParcelRecordsDialog)
        self.addButton.setGeometry(QtCore.QRect(350, 88, 90, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(0, 23))
        self.addButton.setMaximumSize(QtCore.QSize(120, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addButton.setFont(font)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.editButton = QtGui.QPushButton(ManageParcelRecordsDialog)
        self.editButton.setGeometry(QtCore.QRect(350, 118, 90, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setMinimumSize(QtCore.QSize(0, 23))
        self.editButton.setMaximumSize(QtCore.QSize(120, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.editButton.setFont(font)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.deleteButton = QtGui.QPushButton(ManageParcelRecordsDialog)
        self.deleteButton.setGeometry(QtCore.QRect(350, 148, 90, 23))
        self.deleteButton.setMinimumSize(QtCore.QSize(0, 23))
        self.deleteButton.setMaximumSize(QtCore.QSize(120, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.helpButton = QtGui.QPushButton(ManageParcelRecordsDialog)
        self.helpButton.setGeometry(QtCore.QRect(277, 345, 61, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy)
        self.helpButton.setMinimumSize(QtCore.QSize(28, 23))
        self.helpButton.setMaximumSize(QtCore.QSize(70, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.helpButton.setFont(font)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.closeButton = QtGui.QPushButton(ManageParcelRecordsDialog)
        self.closeButton.setGeometry(QtCore.QRect(351, 345, 70, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(70, 23))
        self.closeButton.setMaximumSize(QtCore.QSize(70, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.label = QtGui.QLabel(ManageParcelRecordsDialog)
        self.label.setGeometry(QtCore.QRect(15, 69, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.parcel_type_cbox = QtGui.QComboBox(ManageParcelRecordsDialog)
        self.parcel_type_cbox.setGeometry(QtCore.QRect(15, 40, 226, 20))
        self.parcel_type_cbox.setObjectName(_fromUtf8("parcel_type_cbox"))
        self.line = QtGui.QFrame(ManageParcelRecordsDialog)
        self.line.setGeometry(QtCore.QRect(0, 20, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(ManageParcelRecordsDialog)
        self.line_2.setGeometry(QtCore.QRect(0, 375, 451, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_2 = QtGui.QLabel(ManageParcelRecordsDialog)
        self.label_2.setGeometry(QtCore.QRect(15, 10, 381, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.record_twidget = QtGui.QTableWidget(ManageParcelRecordsDialog)
        self.record_twidget.setGeometry(QtCore.QRect(15, 89, 330, 241))
        self.record_twidget.setObjectName(_fromUtf8("record_twidget"))
        self.record_twidget.setColumnCount(1)
        self.record_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.record_twidget.setHorizontalHeaderItem(0, item)
        self.record_twidget.horizontalHeader().setDefaultSectionSize(320)

        self.retranslateUi(ManageParcelRecordsDialog)
        QtCore.QMetaObject.connectSlotsByName(ManageParcelRecordsDialog)
        ManageParcelRecordsDialog.setTabOrder(self.addButton, self.editButton)
        ManageParcelRecordsDialog.setTabOrder(self.editButton, self.deleteButton)
        ManageParcelRecordsDialog.setTabOrder(self.deleteButton, self.helpButton)
        ManageParcelRecordsDialog.setTabOrder(self.helpButton, self.closeButton)

    def retranslateUi(self, ManageParcelRecordsDialog):
        ManageParcelRecordsDialog.setWindowTitle(_translate("ManageParcelRecordsDialog", "Valuation Records for Parcel:", None))
        self.addButton.setText(_translate("ManageParcelRecordsDialog", "Add", None))
        self.editButton.setText(_translate("ManageParcelRecordsDialog", "Edit", None))
        self.deleteButton.setText(_translate("ManageParcelRecordsDialog", "Delete", None))
        self.helpButton.setText(_translate("ManageParcelRecordsDialog", "?", None))
        self.closeButton.setText(_translate("ManageParcelRecordsDialog", "Close", None))
        self.label.setText(_translate("ManageParcelRecordsDialog", "Records", None))
        self.label_2.setText(_translate("ManageParcelRecordsDialog", "Manage Parcel Records", None))
        item = self.record_twidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageParcelRecordsDialog", "Records Information", None))

