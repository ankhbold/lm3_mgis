# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PersonDialog.ui'
#
# Created: Tue Jan 26 13:14:37 2016
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

class Ui_PersonDialog(object):
    def setupUi(self, PersonDialog):
        PersonDialog.setObjectName(_fromUtf8("PersonDialog"))
        PersonDialog.resize(800, 500)
        PersonDialog.setMinimumSize(QtCore.QSize(800, 500))
        PersonDialog.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/lm2/person.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PersonDialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(PersonDialog)
        self.label.setGeometry(QtCore.QRect(10, 3, 521, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(PersonDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 27, 260, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.person_type_cbox = QtGui.QComboBox(PersonDialog)
        self.person_type_cbox.setGeometry(QtCore.QRect(30, 43, 260, 20))
        self.person_type_cbox.setObjectName(_fromUtf8("person_type_cbox"))
        self.personal_id_edit = QtGui.QLineEdit(PersonDialog)
        self.personal_id_edit.setGeometry(QtCore.QRect(316, 54, 220, 20))
        self.personal_id_edit.setMaxLength(100)
        self.personal_id_edit.setObjectName(_fromUtf8("personal_id_edit"))
        self.groupBox = QtGui.QGroupBox(PersonDialog)
        self.groupBox.setGeometry(QtCore.QRect(540, 21, 251, 416))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.aimag_cbox = QtGui.QComboBox(self.groupBox)
        self.aimag_cbox.setGeometry(QtCore.QRect(26, 30, 220, 20))
        self.aimag_cbox.setObjectName(_fromUtf8("aimag_cbox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(26, 14, 220, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(26, 53, 220, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.soum_cbox = QtGui.QComboBox(self.groupBox)
        self.soum_cbox.setGeometry(QtCore.QRect(26, 69, 220, 20))
        self.soum_cbox.setObjectName(_fromUtf8("soum_cbox"))
        self.bag_cbox = QtGui.QComboBox(self.groupBox)
        self.bag_cbox.setGeometry(QtCore.QRect(26, 108, 220, 20))
        self.bag_cbox.setObjectName(_fromUtf8("bag_cbox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(26, 92, 220, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.khoroolol_cbox = QtGui.QComboBox(self.groupBox)
        self.khoroolol_cbox.setGeometry(QtCore.QRect(26, 147, 220, 20))
        self.khoroolol_cbox.setObjectName(_fromUtf8("khoroolol_cbox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(26, 131, 220, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.town_cbox_l = QtGui.QLabel(self.groupBox)
        self.town_cbox_l.setGeometry(QtCore.QRect(26, 170, 220, 16))
        self.town_cbox_l.setObjectName(_fromUtf8("town_cbox_l"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(26, 209, 220, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(26, 248, 220, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_27 = QtGui.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(26, 287, 220, 16))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.building_edit = QtGui.QLineEdit(self.groupBox)
        self.building_edit.setGeometry(QtCore.QRect(26, 303, 220, 20))
        self.building_edit.setObjectName(_fromUtf8("building_edit"))
        self.entrance_edit = QtGui.QLineEdit(self.groupBox)
        self.entrance_edit.setGeometry(QtCore.QRect(26, 345, 220, 20))
        self.entrance_edit.setText(_fromUtf8(""))
        self.entrance_edit.setObjectName(_fromUtf8("entrance_edit"))
        self.label_28 = QtGui.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(26, 329, 220, 16))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.apartment_edit = QtGui.QLineEdit(self.groupBox)
        self.apartment_edit.setGeometry(QtCore.QRect(26, 387, 220, 20))
        self.apartment_edit.setObjectName(_fromUtf8("apartment_edit"))
        self.label_29 = QtGui.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(26, 371, 220, 16))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.street_name_edit = QtGui.QLineEdit(self.groupBox)
        self.street_name_edit.setGeometry(QtCore.QRect(28, 225, 211, 21))
        self.street_name_edit.setObjectName(_fromUtf8("street_name_edit"))
        self.town_edit = QtGui.QLineEdit(self.groupBox)
        self.town_edit.setGeometry(QtCore.QRect(28, 188, 211, 21))
        self.town_edit.setObjectName(_fromUtf8("town_edit"))
        self.khashaa_edit = QtGui.QLineEdit(self.groupBox)
        self.khashaa_edit.setGeometry(QtCore.QRect(25, 263, 211, 21))
        self.khashaa_edit.setObjectName(_fromUtf8("khashaa_edit"))
        self.close_button = QtGui.QPushButton(PersonDialog)
        self.close_button.setGeometry(QtCore.QRect(718, 452, 75, 23))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.apply_button = QtGui.QPushButton(PersonDialog)
        self.apply_button.setGeometry(QtCore.QRect(636, 452, 75, 23))
        self.apply_button.setObjectName(_fromUtf8("apply_button"))
        self.help_button = QtGui.QPushButton(PersonDialog)
        self.help_button.setGeometry(QtCore.QRect(420, 452, 91, 23))
        self.help_button.setObjectName(_fromUtf8("help_button"))
        self.label_30 = QtGui.QLabel(PersonDialog)
        self.label_30.setGeometry(QtCore.QRect(316, 38, 220, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.state_register_edit = QtGui.QLineEdit(PersonDialog)
        self.state_register_edit.setGeometry(QtCore.QRect(316, 93, 220, 20))
        self.state_register_edit.setMaxLength(10)
        self.state_register_edit.setObjectName(_fromUtf8("state_register_edit"))
        self.label_31 = QtGui.QLabel(PersonDialog)
        self.label_31.setGeometry(QtCore.QRect(316, 77, 220, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(PersonDialog)
        self.label_32.setGeometry(QtCore.QRect(316, 115, 220, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.bank_cbox = QtGui.QComboBox(PersonDialog)
        self.bank_cbox.setGeometry(QtCore.QRect(316, 131, 220, 20))
        self.bank_cbox.setObjectName(_fromUtf8("bank_cbox"))
        self.account_label = QtGui.QLabel(PersonDialog)
        self.account_label.setGeometry(QtCore.QRect(316, 154, 220, 16))
        self.account_label.setObjectName(_fromUtf8("account_label"))
        self.account_edit = QtGui.QLineEdit(PersonDialog)
        self.account_edit.setGeometry(QtCore.QRect(316, 170, 220, 20))
        self.account_edit.setObjectName(_fromUtf8("account_edit"))
        self.phone_label = QtGui.QLabel(PersonDialog)
        self.phone_label.setGeometry(QtCore.QRect(316, 193, 220, 16))
        self.phone_label.setObjectName(_fromUtf8("phone_label"))
        self.phone_edit = QtGui.QLineEdit(PersonDialog)
        self.phone_edit.setGeometry(QtCore.QRect(316, 209, 220, 20))
        self.phone_edit.setObjectName(_fromUtf8("phone_edit"))
        self.label_35 = QtGui.QLabel(PersonDialog)
        self.label_35.setGeometry(QtCore.QRect(316, 232, 220, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.mobile_phone_edit = QtGui.QLineEdit(PersonDialog)
        self.mobile_phone_edit.setGeometry(QtCore.QRect(316, 248, 220, 20))
        self.mobile_phone_edit.setObjectName(_fromUtf8("mobile_phone_edit"))
        self.email_edit = QtGui.QLineEdit(PersonDialog)
        self.email_edit.setGeometry(QtCore.QRect(316, 287, 220, 20))
        self.email_edit.setObjectName(_fromUtf8("email_edit"))
        self.label_36 = QtGui.QLabel(PersonDialog)
        self.label_36.setGeometry(QtCore.QRect(316, 271, 220, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.label_36.setFont(font)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.website_edit = QtGui.QLineEdit(PersonDialog)
        self.website_edit.setGeometry(QtCore.QRect(316, 326, 220, 20))
        self.website_edit.setObjectName(_fromUtf8("website_edit"))
        self.label_37 = QtGui.QLabel(PersonDialog)
        self.label_37.setGeometry(QtCore.QRect(316, 310, 220, 16))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.line = QtGui.QFrame(PersonDialog)
        self.line.setGeometry(QtCore.QRect(0, 11, 791, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(PersonDialog)
        self.line_2.setGeometry(QtCore.QRect(10, 437, 781, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.middle_name_edit = QtGui.QLineEdit(PersonDialog)
        self.middle_name_edit.setGeometry(QtCore.QRect(45, 80, 220, 20))
        self.middle_name_edit.setObjectName(_fromUtf8("middle_name_edit"))
        self.label_39 = QtGui.QLabel(PersonDialog)
        self.label_39.setGeometry(QtCore.QRect(45, 64, 220, 16))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_40 = QtGui.QLabel(PersonDialog)
        self.label_40.setGeometry(QtCore.QRect(45, 143, 220, 16))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.first_name_edit = QtGui.QLineEdit(PersonDialog)
        self.first_name_edit.setGeometry(QtCore.QRect(45, 159, 220, 20))
        self.first_name_edit.setObjectName(_fromUtf8("first_name_edit"))
        self.groupBox_2 = QtGui.QGroupBox(PersonDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 190, 260, 36))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.male_rbutton = QtGui.QRadioButton(self.groupBox_2)
        self.male_rbutton.setGeometry(QtCore.QRect(30, 14, 91, 20))
        self.male_rbutton.setChecked(True)
        self.male_rbutton.setObjectName(_fromUtf8("male_rbutton"))
        self.female_rbutton = QtGui.QRadioButton(self.groupBox_2)
        self.female_rbutton.setGeometry(QtCore.QRect(120, 14, 69, 20))
        self.female_rbutton.setObjectName(_fromUtf8("female_rbutton"))
        self.label_41 = QtGui.QLabel(PersonDialog)
        self.label_41.setGeometry(QtCore.QRect(45, 230, 220, 16))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.date_of_birth_date = QtGui.QDateEdit(PersonDialog)
        self.date_of_birth_date.setGeometry(QtCore.QRect(45, 246, 220, 20))
        self.date_of_birth_date.setLocale(QtCore.QLocale(QtCore.QLocale.Mongolian, QtCore.QLocale.Mongolia))
        self.date_of_birth_date.setDisplayFormat(_fromUtf8("yyyy-MM-dd"))
        self.date_of_birth_date.setCalendarPopup(True)
        self.date_of_birth_date.setObjectName(_fromUtf8("date_of_birth_date"))
        self.contact_person_group_box = QtGui.QGroupBox(PersonDialog)
        self.contact_person_group_box.setEnabled(True)
        self.contact_person_group_box.setGeometry(QtCore.QRect(30, 270, 260, 151))
        self.contact_person_group_box.setObjectName(_fromUtf8("contact_person_group_box"))
        self.contact_surname_label = QtGui.QLabel(self.contact_person_group_box)
        self.contact_surname_label.setGeometry(QtCore.QRect(15, 20, 220, 16))
        self.contact_surname_label.setObjectName(_fromUtf8("contact_surname_label"))
        self.label_43 = QtGui.QLabel(self.contact_person_group_box)
        self.label_43.setGeometry(QtCore.QRect(15, 97, 220, 16))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.contact_surname_edit = QtGui.QLineEdit(self.contact_person_group_box)
        self.contact_surname_edit.setGeometry(QtCore.QRect(15, 36, 220, 20))
        self.contact_surname_edit.setObjectName(_fromUtf8("contact_surname_edit"))
        self.contact_position_edit = QtGui.QLineEdit(self.contact_person_group_box)
        self.contact_position_edit.setGeometry(QtCore.QRect(15, 113, 220, 20))
        self.contact_position_edit.setObjectName(_fromUtf8("contact_position_edit"))
        self.label_44 = QtGui.QLabel(self.contact_person_group_box)
        self.label_44.setGeometry(QtCore.QRect(15, 58, 220, 16))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.contact_first_name_edit = QtGui.QLineEdit(self.contact_person_group_box)
        self.contact_first_name_edit.setGeometry(QtCore.QRect(15, 74, 220, 20))
        self.contact_first_name_edit.setObjectName(_fromUtf8("contact_first_name_edit"))
        self.error_label = QtGui.QLabel(PersonDialog)
        self.error_label.setGeometry(QtCore.QRect(30, 450, 391, 41))
        self.error_label.setText(_fromUtf8(""))
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName(_fromUtf8("error_label"))
        self.status_label = QtGui.QLabel(PersonDialog)
        self.status_label.setGeometry(QtCore.QRect(30, 460, 211, 20))
        self.status_label.setText(_fromUtf8(""))
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.apply_clear_button = QtGui.QPushButton(PersonDialog)
        self.apply_clear_button.setGeometry(QtCore.QRect(514, 452, 121, 23))
        self.apply_clear_button.setObjectName(_fromUtf8("apply_clear_button"))
        self.surname_company_edit = QtGui.QLineEdit(PersonDialog)
        self.surname_company_edit.setGeometry(QtCore.QRect(45, 119, 220, 20))
        self.surname_company_edit.setInputMask(_fromUtf8(""))
        self.surname_company_edit.setObjectName(_fromUtf8("surname_company_edit"))
        self.label_38 = QtGui.QLabel(PersonDialog)
        self.label_38.setGeometry(QtCore.QRect(45, 103, 239, 16))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.country_cbox = QtGui.QComboBox(PersonDialog)
        self.country_cbox.setGeometry(QtCore.QRect(316, 369, 220, 22))
        self.country_cbox.setObjectName(_fromUtf8("country_cbox"))
        self.label_7 = QtGui.QLabel(PersonDialog)
        self.label_7.setGeometry(QtCore.QRect(316, 351, 211, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(PersonDialog)
        QtCore.QMetaObject.connectSlotsByName(PersonDialog)
        PersonDialog.setTabOrder(self.person_type_cbox, self.middle_name_edit)
        PersonDialog.setTabOrder(self.middle_name_edit, self.surname_company_edit)
        PersonDialog.setTabOrder(self.surname_company_edit, self.first_name_edit)
        PersonDialog.setTabOrder(self.first_name_edit, self.male_rbutton)
        PersonDialog.setTabOrder(self.male_rbutton, self.female_rbutton)
        PersonDialog.setTabOrder(self.female_rbutton, self.date_of_birth_date)
        PersonDialog.setTabOrder(self.date_of_birth_date, self.contact_surname_edit)
        PersonDialog.setTabOrder(self.contact_surname_edit, self.contact_first_name_edit)
        PersonDialog.setTabOrder(self.contact_first_name_edit, self.contact_position_edit)
        PersonDialog.setTabOrder(self.contact_position_edit, self.personal_id_edit)
        PersonDialog.setTabOrder(self.personal_id_edit, self.state_register_edit)
        PersonDialog.setTabOrder(self.state_register_edit, self.bank_cbox)
        PersonDialog.setTabOrder(self.bank_cbox, self.account_edit)
        PersonDialog.setTabOrder(self.account_edit, self.phone_edit)
        PersonDialog.setTabOrder(self.phone_edit, self.mobile_phone_edit)
        PersonDialog.setTabOrder(self.mobile_phone_edit, self.email_edit)
        PersonDialog.setTabOrder(self.email_edit, self.website_edit)
        PersonDialog.setTabOrder(self.website_edit, self.aimag_cbox)
        PersonDialog.setTabOrder(self.aimag_cbox, self.soum_cbox)
        PersonDialog.setTabOrder(self.soum_cbox, self.bag_cbox)
        PersonDialog.setTabOrder(self.bag_cbox, self.khoroolol_cbox)
        PersonDialog.setTabOrder(self.khoroolol_cbox, self.town_edit)
        PersonDialog.setTabOrder(self.town_edit, self.street_name_edit)
        PersonDialog.setTabOrder(self.street_name_edit, self.khashaa_edit)
        PersonDialog.setTabOrder(self.khashaa_edit, self.building_edit)
        PersonDialog.setTabOrder(self.building_edit, self.entrance_edit)
        PersonDialog.setTabOrder(self.entrance_edit, self.apartment_edit)
        PersonDialog.setTabOrder(self.apartment_edit, self.apply_button)
        PersonDialog.setTabOrder(self.apply_button, self.close_button)
        PersonDialog.setTabOrder(self.close_button, self.apply_clear_button)
        PersonDialog.setTabOrder(self.apply_clear_button, self.help_button)

    def retranslateUi(self, PersonDialog):
        PersonDialog.setWindowTitle(_translate("PersonDialog", "Dialog", None))
        self.label.setText(_translate("PersonDialog", "Person", None))
        self.label_2.setText(_translate("PersonDialog", "Person Type", None))
        self.groupBox.setTitle(_translate("PersonDialog", "Address", None))
        self.label_3.setText(_translate("PersonDialog", "Aimag / Duureg", None))
        self.label_4.setText(_translate("PersonDialog", "Soum", None))
        self.label_5.setText(_translate("PersonDialog", "Bag / Khoroo", None))
        self.label_6.setText(_translate("PersonDialog", "Khoroolol", None))
        self.town_cbox_l.setText(_translate("PersonDialog", "Town / Local Name", None))
        self.label_12.setText(_translate("PersonDialog", "Street Name", None))
        self.label_19.setText(_translate("PersonDialog", "Khashaa", None))
        self.label_27.setText(_translate("PersonDialog", "Building Number", None))
        self.label_28.setText(_translate("PersonDialog", "Entrance Number", None))
        self.label_29.setText(_translate("PersonDialog", "Apartment Number", None))
        self.close_button.setText(_translate("PersonDialog", "Close", None))
        self.apply_button.setText(_translate("PersonDialog", "Apply", None))
        self.help_button.setText(_translate("PersonDialog", "?", None))
        self.label_30.setText(_translate("PersonDialog", "Personal ID / Company ID", None))
        self.label_31.setText(_translate("PersonDialog", "State Registration Number", None))
        self.label_32.setText(_translate("PersonDialog", "Bank", None))
        self.account_label.setText(_translate("PersonDialog", "Bank Account Number", None))
        self.phone_label.setText(_translate("PersonDialog", "Phone(s) [comma-separated]", None))
        self.label_35.setText(_translate("PersonDialog", "Mobile Phone(s)  [comma-separated]", None))
        self.label_36.setText(_translate("PersonDialog", "Email Address(s) [comma-separated]", None))
        self.label_37.setText(_translate("PersonDialog", "WebSite", None))
        self.label_39.setText(_translate("PersonDialog", "Middle Name", None))
        self.label_40.setText(_translate("PersonDialog", "First Name", None))
        self.groupBox_2.setTitle(_translate("PersonDialog", "Gender", None))
        self.male_rbutton.setText(_translate("PersonDialog", "Male", None))
        self.female_rbutton.setText(_translate("PersonDialog", "Female", None))
        self.label_41.setText(_translate("PersonDialog", "Date Of Birth", None))
        self.contact_person_group_box.setTitle(_translate("PersonDialog", "Contact Person (Company / Organization)", None))
        self.contact_surname_label.setText(_translate("PersonDialog", "Surname", None))
        self.label_43.setText(_translate("PersonDialog", "Position", None))
        self.label_44.setText(_translate("PersonDialog", "First Name", None))
        self.apply_clear_button.setText(_translate("PersonDialog", "Apply and Clear", None))
        self.label_38.setText(_translate("PersonDialog", "Surname or Company/Organization Name", None))
        self.label_7.setText(_translate("PersonDialog", "Country", None))

import resources_rc
