# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PrintPointDialog.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
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

class Ui_PrintPointDialog(object):
    def setupUi(self, PrintPointDialog):
        PrintPointDialog.setObjectName(_fromUtf8("PrintPointDialog"))
        PrintPointDialog.resize(506, 630)
        PrintPointDialog.setMinimumSize(QtCore.QSize(506, 500))
        PrintPointDialog.setMaximumSize(QtCore.QSize(506, 800))
        self.about_button = QtGui.QPushButton(PrintPointDialog)
        self.about_button.setGeometry(QtCore.QRect(331, 600, 75, 23))
        self.about_button.setObjectName(_fromUtf8("about_button"))
        self.close_button = QtGui.QPushButton(PrintPointDialog)
        self.close_button.setGeometry(QtCore.QRect(421, 600, 75, 23))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.line = QtGui.QFrame(PrintPointDialog)
        self.line.setGeometry(QtCore.QRect(0, 18, 505, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(PrintPointDialog)
        self.line_2.setGeometry(QtCore.QRect(1, 584, 505, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget = QtGui.QTabWidget(PrintPointDialog)
        self.tabWidget.setGeometry(QtCore.QRect(6, 220, 497, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(62, 30, 416, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 414, 319))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.prev_button = QtGui.QPushButton(self.tab)
        self.prev_button.setGeometry(QtCore.QRect(323, 354, 75, 23))
        self.prev_button.setObjectName(_fromUtf8("prev_button"))
        self.fit_button = QtGui.QPushButton(self.tab)
        self.fit_button.setGeometry(QtCore.QRect(6, 132, 50, 50))
        self.fit_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/lm2_pasture/zoom_fit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fit_button.setIcon(icon)
        self.fit_button.setIconSize(QtCore.QSize(32, 32))
        self.fit_button.setObjectName(_fromUtf8("fit_button"))
        self.imageLabel = QtGui.QLabel(self.tab)
        self.imageLabel.setGeometry(QtCore.QRect(74, 44, 381, 291))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.count_label = QtGui.QLabel(self.tab)
        self.count_label.setGeometry(QtCore.QRect(273, 357, 51, 16))
        self.count_label.setObjectName(_fromUtf8("count_label"))
        self.cover_rbutton = QtGui.QRadioButton(self.tab)
        self.cover_rbutton.setGeometry(QtCore.QRect(224, 6, 75, 17))
        self.cover_rbutton.setObjectName(_fromUtf8("cover_rbutton"))
        self.zoomout_button = QtGui.QPushButton(self.tab)
        self.zoomout_button.setGeometry(QtCore.QRect(6, 81, 50, 50))
        self.zoomout_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/lm2_pasture/zoom_out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomout_button.setIcon(icon1)
        self.zoomout_button.setIconSize(QtCore.QSize(32, 32))
        self.zoomout_button.setObjectName(_fromUtf8("zoomout_button"))
        self.load_image_button = QtGui.QPushButton(self.tab)
        self.load_image_button.setGeometry(QtCore.QRect(404, 4, 75, 23))
        self.load_image_button.setObjectName(_fromUtf8("load_image_button"))
        self.around_rbutton = QtGui.QRadioButton(self.tab)
        self.around_rbutton.setGeometry(QtCore.QRect(314, 6, 75, 17))
        self.around_rbutton.setObjectName(_fromUtf8("around_rbutton"))
        self.zoomin_button = QtGui.QPushButton(self.tab)
        self.zoomin_button.setGeometry(QtCore.QRect(6, 30, 50, 50))
        self.zoomin_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/lm2_pasture/zoom_in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomin_button.setIcon(icon2)
        self.zoomin_button.setIconSize(QtCore.QSize(32, 32))
        self.zoomin_button.setObjectName(_fromUtf8("zoomin_button"))
        self.next_button = QtGui.QPushButton(self.tab)
        self.next_button.setGeometry(QtCore.QRect(403, 354, 75, 23))
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.print_button = QtGui.QPushButton(self.tab)
        self.print_button.setGeometry(QtCore.QRect(6, 183, 50, 50))
        self.print_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/lm2_pasture/printer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_button.setIcon(icon3)
        self.print_button.setIconSize(QtCore.QSize(32, 32))
        self.print_button.setObjectName(_fromUtf8("print_button"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(5, 5, 481, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_49 = QtGui.QLabel(self.groupBox)
        self.label_49.setGeometry(QtCore.QRect(220, 110, 241, 16))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_40 = QtGui.QLabel(self.groupBox)
        self.label_40.setGeometry(QtCore.QRect(220, 21, 241, 16))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_31 = QtGui.QLabel(self.groupBox)
        self.label_31.setGeometry(QtCore.QRect(10, 81, 81, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.calc_d1_100ga_edit = QtGui.QLineEdit(self.groupBox)
        self.calc_d1_100ga_edit.setGeometry(QtCore.QRect(90, 50, 120, 20))
        self.calc_d1_100ga_edit.setReadOnly(True)
        self.calc_d1_100ga_edit.setObjectName(_fromUtf8("calc_d1_100ga_edit"))
        self.calc_unelgee_edit = QtGui.QLineEdit(self.groupBox)
        self.calc_unelgee_edit.setGeometry(QtCore.QRect(90, 139, 120, 20))
        self.calc_unelgee_edit.setReadOnly(True)
        self.calc_unelgee_edit.setObjectName(_fromUtf8("calc_unelgee_edit"))
        self.label_47 = QtGui.QLabel(self.groupBox)
        self.label_47.setGeometry(QtCore.QRect(220, 51, 241, 16))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.calc_d1_edit = QtGui.QLineEdit(self.groupBox)
        self.calc_d1_edit.setGeometry(QtCore.QRect(90, 20, 120, 20))
        self.calc_d1_edit.setReadOnly(True)
        self.calc_d1_edit.setObjectName(_fromUtf8("calc_d1_edit"))
        self.label_32 = QtGui.QLabel(self.groupBox)
        self.label_32.setGeometry(QtCore.QRect(10, 111, 81, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_37 = QtGui.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.calc_d2_edit = QtGui.QLineEdit(self.groupBox)
        self.calc_d2_edit.setGeometry(QtCore.QRect(90, 80, 120, 20))
        self.calc_d2_edit.setReadOnly(True)
        self.calc_d2_edit.setObjectName(_fromUtf8("calc_d2_edit"))
        self.label_51 = QtGui.QLabel(self.groupBox)
        self.label_51.setGeometry(QtCore.QRect(220, 140, 241, 16))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_26 = QtGui.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(10, 24, 81, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_48 = QtGui.QLabel(self.groupBox)
        self.label_48.setGeometry(QtCore.QRect(220, 80, 241, 16))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.label_30 = QtGui.QLabel(self.groupBox)
        self.label_30.setGeometry(QtCore.QRect(10, 51, 81, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.calc_d3_edit = QtGui.QLineEdit(self.groupBox)
        self.calc_d3_edit.setGeometry(QtCore.QRect(90, 110, 120, 20))
        self.calc_d3_edit.setReadOnly(True)
        self.calc_d3_edit.setObjectName(_fromUtf8("calc_d3_edit"))
        self.calc_duration_sbox = QtGui.QSpinBox(self.groupBox)
        self.calc_duration_sbox.setEnabled(True)
        self.calc_duration_sbox.setGeometry(QtCore.QRect(90, 170, 121, 22))
        self.calc_duration_sbox.setReadOnly(False)
        self.calc_duration_sbox.setMaximum(1000000000)
        self.calc_duration_sbox.setObjectName(_fromUtf8("calc_duration_sbox"))
        self.label_38 = QtGui.QLabel(self.groupBox)
        self.label_38.setGeometry(QtCore.QRect(10, 172, 81, 16))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_52 = QtGui.QLabel(self.groupBox)
        self.label_52.setGeometry(QtCore.QRect(220, 172, 241, 16))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(5, 220, 481, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(180, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 148, 81))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_3 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.point_address_label = QtGui.QLabel(PrintPointDialog)
        self.point_address_label.setGeometry(QtCore.QRect(5, 28, 496, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.point_address_label.setFont(font)
        self.point_address_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.point_address_label.setTextFormat(QtCore.Qt.AutoText)
        self.point_address_label.setAlignment(QtCore.Qt.AlignCenter)
        self.point_address_label.setWordWrap(False)
        self.point_address_label.setObjectName(_fromUtf8("point_address_label"))
        self.land_form_label = QtGui.QLabel(PrintPointDialog)
        self.land_form_label.setGeometry(QtCore.QRect(5, 60, 496, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.land_form_label.setFont(font)
        self.land_form_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.land_form_label.setObjectName(_fromUtf8("land_form_label"))
        self.label_2 = QtGui.QLabel(PrintPointDialog)
        self.label_2.setGeometry(QtCore.QRect(8, 7, 330, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(PrintPointDialog)
        self.label.setGeometry(QtCore.QRect(10, 95, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.year_sbox = QtGui.QSpinBox(PrintPointDialog)
        self.year_sbox.setGeometry(QtCore.QRect(90, 93, 55, 20))
        self.year_sbox.setMinimum(1900)
        self.year_sbox.setMaximum(2100)
        self.year_sbox.setProperty("value", 2017)
        self.year_sbox.setObjectName(_fromUtf8("year_sbox"))
        self.load_data_button = QtGui.QPushButton(PrintPointDialog)
        self.load_data_button.setGeometry(QtCore.QRect(170, 92, 131, 23))
        self.load_data_button.setObjectName(_fromUtf8("load_data_button"))
        self.label_3 = QtGui.QLabel(PrintPointDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 74, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(PrintPointDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 74, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(PrintPointDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 74, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.biomass_label = QtGui.QLabel(PrintPointDialog)
        self.biomass_label.setGeometry(QtCore.QRect(90, 140, 74, 13))
        self.biomass_label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.biomass_label.setObjectName(_fromUtf8("biomass_label"))
        self.rc_label = QtGui.QLabel(PrintPointDialog)
        self.rc_label.setGeometry(QtCore.QRect(90, 120, 74, 13))
        self.rc_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rc_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.rc_label.setObjectName(_fromUtf8("rc_label"))
        self.cover_label = QtGui.QLabel(PrintPointDialog)
        self.cover_label.setGeometry(QtCore.QRect(90, 160, 74, 13))
        self.cover_label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.cover_label.setObjectName(_fromUtf8("cover_label"))
        self.cover_label_2 = QtGui.QLabel(PrintPointDialog)
        self.cover_label_2.setGeometry(QtCore.QRect(90, 200, 74, 13))
        self.cover_label_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.cover_label_2.setText(_fromUtf8(""))
        self.cover_label_2.setObjectName(_fromUtf8("cover_label_2"))
        self.biomass_label_2 = QtGui.QLabel(PrintPointDialog)
        self.biomass_label_2.setGeometry(QtCore.QRect(91, 180, 74, 13))
        self.biomass_label_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.biomass_label_2.setText(_fromUtf8(""))
        self.biomass_label_2.setObjectName(_fromUtf8("biomass_label_2"))
        self.label_6 = QtGui.QLabel(PrintPointDialog)
        self.label_6.setGeometry(QtCore.QRect(11, 180, 74, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(PrintPointDialog)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 74, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(PrintPointDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PrintPointDialog)

    def retranslateUi(self, PrintPointDialog):
        PrintPointDialog.setWindowTitle(_translate("PrintPointDialog", "Dialog", None))
        self.about_button.setText(_translate("PrintPointDialog", "About", None))
        self.close_button.setText(_translate("PrintPointDialog", "close", None))
        self.prev_button.setText(_translate("PrintPointDialog", "Prev", None))
        self.imageLabel.setText(_translate("PrintPointDialog", "Image Viewer", None))
        self.count_label.setText(_translate("PrintPointDialog", "Count", None))
        self.cover_rbutton.setText(_translate("PrintPointDialog", "Cover", None))
        self.load_image_button.setText(_translate("PrintPointDialog", "Load Image", None))
        self.around_rbutton.setText(_translate("PrintPointDialog", "Around", None))
        self.next_button.setText(_translate("PrintPointDialog", "Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PrintPointDialog", "Point Information", None))
        self.groupBox.setTitle(_translate("PrintPointDialog", "Calculate Values", None))
        self.label_49.setText(_translate("PrintPointDialog", "Боломжит даац", None))
        self.label_40.setText(_translate("PrintPointDialog", "1 га-д бэлчиж болох хонин толгой", None))
        self.label_31.setText(_translate("PrintPointDialog", "D-2:", None))
        self.label_47.setText(_translate("PrintPointDialog", "100 га-д бэлчиж болох хонин толгой", None))
        self.label_32.setText(_translate("PrintPointDialog", "D-3:", None))
        self.label_37.setText(_translate("PrintPointDialog", "Unelgee:", None))
        self.label_51.setText(_translate("PrintPointDialog", "Боломжит ХТ- Одоо байгаа ХТ = Үнэлгээ", None))
        self.label_26.setText(_translate("PrintPointDialog", "D-1:", None))
        self.label_48.setText(_translate("PrintPointDialog", "1 хонин толгойд шаардлагатай талбай", None))
        self.label_30.setText(_translate("PrintPointDialog", "D-1-100ga:", None))
        self.label_38.setText(_translate("PrintPointDialog", "Duration:", None))
        self.label_52.setText(_translate("PrintPointDialog", "Мал бэлчээрлэх хугацаа /хоногоор/", None))
        self.groupBox_2.setTitle(_translate("PrintPointDialog", "Print Pasture", None))
        self.pushButton.setText(_translate("PrintPointDialog", "Print", None))
        self.radioButton_3.setText(_translate("PrintPointDialog", "БАХ-н бэлчээр", None))
        self.radioButton_2.setText(_translate("PrintPointDialog", "Улирлын бэлчээр", None))
        self.radioButton.setText(_translate("PrintPointDialog", "Сэргэх чадавхийн зураг", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PrintPointDialog", "Pasture Information", None))
        self.point_address_label.setText(_translate("PrintPointDialog", "Address", None))
        self.land_form_label.setText(_translate("PrintPointDialog", "Land Form", None))
        self.label_2.setText(_translate("PrintPointDialog", "Point Information", None))
        self.label.setText(_translate("PrintPointDialog", "Year", None))
        self.load_data_button.setText(_translate("PrintPointDialog", "Load Data", None))
        self.label_3.setText(_translate("PrintPointDialog", "Recovery Class", None))
        self.label_4.setText(_translate("PrintPointDialog", "Bio Mass", None))
        self.label_5.setText(_translate("PrintPointDialog", "Total Cover", None))
        self.biomass_label.setText(_translate("PrintPointDialog", "Bio Mass", None))
        self.rc_label.setText(_translate("PrintPointDialog", "Recovery Class", None))
        self.cover_label.setText(_translate("PrintPointDialog", "Total Cover", None))
        self.label_6.setText(_translate("PrintPointDialog", "PUG", None))
        self.label_7.setText(_translate("PrintPointDialog", "Pasture Type", None))

import resources_pasture_rc