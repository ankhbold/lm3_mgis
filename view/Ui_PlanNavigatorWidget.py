# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PlanNavigatorWidget.ui'
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

class Ui_PlanNavigatorWidget(object):
    def setupUi(self, PlanNavigatorWidget):
        PlanNavigatorWidget.setObjectName(_fromUtf8("PlanNavigatorWidget"))
        PlanNavigatorWidget.resize(415, 712)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlanNavigatorWidget.sizePolicy().hasHeightForWidth())
        PlanNavigatorWidget.setSizePolicy(sizePolicy)
        PlanNavigatorWidget.setMinimumSize(QtCore.QSize(415, 620))
        PlanNavigatorWidget.setMaximumSize(QtCore.QSize(415, 524287))
        PlanNavigatorWidget.setBaseSize(QtCore.QSize(440, 665))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 418, 650))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 600))
        self.scrollArea.setMaximumSize(QtCore.QSize(435, 650))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 664))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.tabWidget = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(6, 0, 386, 625))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 625))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.plan_tab = QtGui.QWidget()
        self.plan_tab.setObjectName(_fromUtf8("plan_tab"))
        self.groupBox_11 = QtGui.QGroupBox(self.plan_tab)
        self.groupBox_11.setGeometry(QtCore.QRect(5, 30, 371, 231))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.plan_num_edit = QtGui.QLineEdit(self.groupBox_11)
        self.plan_num_edit.setGeometry(QtCore.QRect(190, 25, 170, 20))
        self.plan_num_edit.setObjectName(_fromUtf8("plan_num_edit"))
        self.label_31 = QtGui.QLabel(self.groupBox_11)
        self.label_31.setGeometry(QtCore.QRect(10, 82, 171, 17))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.groupBox_11)
        self.label_32.setGeometry(QtCore.QRect(10, 160, 171, 17))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_34 = QtGui.QLabel(self.groupBox_11)
        self.label_34.setGeometry(QtCore.QRect(190, 8, 171, 17))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.office_in_charge_cbox = QtGui.QComboBox(self.groupBox_11)
        self.office_in_charge_cbox.setGeometry(QtCore.QRect(10, 180, 170, 21))
        self.office_in_charge_cbox.setObjectName(_fromUtf8("office_in_charge_cbox"))
        self.status_cbox = QtGui.QComboBox(self.groupBox_11)
        self.status_cbox.setGeometry(QtCore.QRect(10, 99, 351, 21))
        self.status_cbox.setObjectName(_fromUtf8("status_cbox"))
        self.plan_results_label = QtGui.QLabel(self.groupBox_11)
        self.plan_results_label.setGeometry(QtCore.QRect(10, 206, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plan_results_label.setFont(font)
        self.plan_results_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.plan_results_label.setObjectName(_fromUtf8("plan_results_label"))
        self.next_officer_in_charge_cbox = QtGui.QComboBox(self.groupBox_11)
        self.next_officer_in_charge_cbox.setGeometry(QtCore.QRect(190, 180, 170, 21))
        self.next_officer_in_charge_cbox.setObjectName(_fromUtf8("next_officer_in_charge_cbox"))
        self.label_37 = QtGui.QLabel(self.groupBox_11)
        self.label_37.setGeometry(QtCore.QRect(190, 160, 171, 17))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.label_55 = QtGui.QLabel(self.groupBox_11)
        self.label_55.setGeometry(QtCore.QRect(10, 42, 171, 20))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.plan_type_cbox = QtGui.QComboBox(self.groupBox_11)
        self.plan_type_cbox.setGeometry(QtCore.QRect(10, 60, 351, 23))
        self.plan_type_cbox.setObjectName(_fromUtf8("plan_type_cbox"))
        self.plan_date_checkbox = QtGui.QCheckBox(self.groupBox_11)
        self.plan_date_checkbox.setGeometry(QtCore.QRect(10, 24, 81, 20))
        self.plan_date_checkbox.setObjectName(_fromUtf8("plan_date_checkbox"))
        self.plan_datetime_edit = QtGui.QDateEdit(self.groupBox_11)
        self.plan_datetime_edit.setEnabled(False)
        self.plan_datetime_edit.setGeometry(QtCore.QRect(100, 25, 81, 20))
        self.plan_datetime_edit.setObjectName(_fromUtf8("plan_datetime_edit"))
        self.label_33 = QtGui.QLabel(self.groupBox_11)
        self.label_33.setGeometry(QtCore.QRect(10, 121, 171, 17))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.decision_level_cbox = QtGui.QComboBox(self.groupBox_11)
        self.decision_level_cbox.setGeometry(QtCore.QRect(10, 138, 351, 21))
        self.decision_level_cbox.setObjectName(_fromUtf8("decision_level_cbox"))
        self.plan_find_button = QtGui.QPushButton(self.plan_tab)
        self.plan_find_button.setGeometry(QtCore.QRect(291, 234, 75, 23))
        self.plan_find_button.setAutoDefault(True)
        self.plan_find_button.setDefault(True)
        self.plan_find_button.setObjectName(_fromUtf8("plan_find_button"))
        self.plan_clear_button = QtGui.QPushButton(self.plan_tab)
        self.plan_clear_button.setGeometry(QtCore.QRect(205, 234, 75, 23))
        self.plan_clear_button.setObjectName(_fromUtf8("plan_clear_button"))
        self.groupBox_12 = QtGui.QGroupBox(self.plan_tab)
        self.groupBox_12.setGeometry(QtCore.QRect(5, 260, 371, 301))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.plan_results_twidget = QtGui.QTableWidget(self.groupBox_12)
        self.plan_results_twidget.setGeometry(QtCore.QRect(5, 18, 361, 241))
        self.plan_results_twidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.plan_results_twidget.setObjectName(_fromUtf8("plan_results_twidget"))
        self.plan_results_twidget.setColumnCount(0)
        self.plan_results_twidget.setRowCount(0)
        self.current_view_button = QtGui.QPushButton(self.groupBox_12)
        self.current_view_button.setGeometry(QtCore.QRect(260, 270, 100, 23))
        self.current_view_button.setObjectName(_fromUtf8("current_view_button"))
        self.plan_edit_button = QtGui.QPushButton(self.groupBox_12)
        self.plan_edit_button.setGeometry(QtCore.QRect(140, 270, 100, 23))
        self.plan_edit_button.setObjectName(_fromUtf8("plan_edit_button"))
        self.case_button = QtGui.QPushButton(self.groupBox_12)
        self.case_button.setGeometry(QtCore.QRect(15, 270, 100, 23))
        self.case_button.setObjectName(_fromUtf8("case_button"))
        self.working_l2_cbox = QtGui.QComboBox(self.plan_tab)
        self.working_l2_cbox.setGeometry(QtCore.QRect(236, 5, 140, 22))
        self.working_l2_cbox.setObjectName(_fromUtf8("working_l2_cbox"))
        self.working_l1_cbox = QtGui.QComboBox(self.plan_tab)
        self.working_l1_cbox.setGeometry(QtCore.QRect(88, 5, 140, 22))
        self.working_l1_cbox.setObjectName(_fromUtf8("working_l1_cbox"))
        self.error_label = QtGui.QLabel(self.plan_tab)
        self.error_label.setGeometry(QtCore.QRect(7, 568, 374, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet(_fromUtf8("QLabel {color : red;}\n"
"font: 75 14pt \"Helvetica\";"))
        self.error_label.setText(_fromUtf8(""))
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName(_fromUtf8("error_label"))
        self.is_filter_chbox = QtGui.QCheckBox(self.plan_tab)
        self.is_filter_chbox.setGeometry(QtCore.QRect(8, 8, 78, 17))
        self.is_filter_chbox.setObjectName(_fromUtf8("is_filter_chbox"))
        self.tabWidget.addTab(self.plan_tab, _fromUtf8(""))
        self.st_tm_filter_tab = QtGui.QWidget()
        self.st_tm_filter_tab.setObjectName(_fromUtf8("st_tm_filter_tab"))
        self.spatial_groupbox = QtGui.QGroupBox(self.st_tm_filter_tab)
        self.spatial_groupbox.setGeometry(QtCore.QRect(5, 0, 371, 151))
        self.spatial_groupbox.setObjectName(_fromUtf8("spatial_groupbox"))
        self.get_extent_button = QtGui.QPushButton(self.spatial_groupbox)
        self.get_extent_button.setGeometry(QtCore.QRect(129, 53, 111, 28))
        self.get_extent_button.setObjectName(_fromUtf8("get_extent_button"))
        self.apply_button = QtGui.QPushButton(self.spatial_groupbox)
        self.apply_button.setGeometry(QtCore.QRect(10, 120, 110, 23))
        self.apply_button.setObjectName(_fromUtf8("apply_button"))
        self.clear_b_box_button = QtGui.QPushButton(self.spatial_groupbox)
        self.clear_b_box_button.setGeometry(QtCore.QRect(250, 120, 110, 23))
        self.clear_b_box_button.setObjectName(_fromUtf8("clear_b_box_button"))
        self.remove_button = QtGui.QPushButton(self.spatial_groupbox)
        self.remove_button.setGeometry(QtCore.QRect(130, 120, 110, 23))
        self.remove_button.setObjectName(_fromUtf8("remove_button"))
        self.extent_rbutton = QtGui.QRadioButton(self.spatial_groupbox)
        self.extent_rbutton.setGeometry(QtCore.QRect(13, 14, 321, 16))
        self.extent_rbutton.setChecked(True)
        self.extent_rbutton.setObjectName(_fromUtf8("extent_rbutton"))
        self.buttonGroup = QtGui.QButtonGroup(PlanNavigatorWidget)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.extent_rbutton)
        self.extent_east_spinbox = QtGui.QDoubleSpinBox(self.spatial_groupbox)
        self.extent_east_spinbox.setGeometry(QtCore.QRect(250, 57, 110, 20))
        self.extent_east_spinbox.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.extent_east_spinbox.setReadOnly(True)
        self.extent_east_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.extent_east_spinbox.setMinimum(-200000010.0)
        self.extent_east_spinbox.setMaximum(200000010.0)
        self.extent_east_spinbox.setObjectName(_fromUtf8("extent_east_spinbox"))
        self.extent_west_spinbox = QtGui.QDoubleSpinBox(self.spatial_groupbox)
        self.extent_west_spinbox.setGeometry(QtCore.QRect(10, 58, 110, 20))
        self.extent_west_spinbox.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.extent_west_spinbox.setReadOnly(True)
        self.extent_west_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.extent_west_spinbox.setMinimum(-200000010.0)
        self.extent_west_spinbox.setMaximum(200000010.0)
        self.extent_west_spinbox.setObjectName(_fromUtf8("extent_west_spinbox"))
        self.extent_south_spinbox = QtGui.QDoubleSpinBox(self.spatial_groupbox)
        self.extent_south_spinbox.setGeometry(QtCore.QRect(132, 85, 110, 20))
        self.extent_south_spinbox.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.extent_south_spinbox.setReadOnly(True)
        self.extent_south_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.extent_south_spinbox.setMinimum(-200000010.0)
        self.extent_south_spinbox.setMaximum(200000010.0)
        self.extent_south_spinbox.setObjectName(_fromUtf8("extent_south_spinbox"))
        self.extent_north_spinbox = QtGui.QDoubleSpinBox(self.spatial_groupbox)
        self.extent_north_spinbox.setGeometry(QtCore.QRect(130, 28, 110, 20))
        self.extent_north_spinbox.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.extent_north_spinbox.setReadOnly(True)
        self.extent_north_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.extent_north_spinbox.setMinimum(-200000010.0)
        self.extent_north_spinbox.setMaximum(200000010.0)
        self.extent_north_spinbox.setObjectName(_fromUtf8("extent_north_spinbox"))
        self.groupBox_6 = QtGui.QGroupBox(self.st_tm_filter_tab)
        self.groupBox_6.setGeometry(QtCore.QRect(5, 150, 371, 82))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.from_date_edit = QtGui.QDateEdit(self.groupBox_6)
        self.from_date_edit.setGeometry(QtCore.QRect(120, 14, 91, 22))
        self.from_date_edit.setCalendarPopup(True)
        self.from_date_edit.setObjectName(_fromUtf8("from_date_edit"))
        self.till_date_edit = QtGui.QDateEdit(self.groupBox_6)
        self.till_date_edit.setGeometry(QtCore.QRect(120, 40, 91, 22))
        self.till_date_edit.setCalendarPopup(True)
        self.till_date_edit.setObjectName(_fromUtf8("till_date_edit"))
        self.infinity_check_box = QtGui.QCheckBox(self.groupBox_6)
        self.infinity_check_box.setGeometry(QtCore.QRect(20, 40, 91, 20))
        self.infinity_check_box.setObjectName(_fromUtf8("infinity_check_box"))
        self.temp_filter_apply_button = QtGui.QPushButton(self.groupBox_6)
        self.temp_filter_apply_button.setGeometry(QtCore.QRect(240, 40, 91, 23))
        self.temp_filter_apply_button.setObjectName(_fromUtf8("temp_filter_apply_button"))
        self.label_12 = QtGui.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(20, 18, 101, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tabWidget_2 = QtGui.QTabWidget(self.st_tm_filter_tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 240, 381, 351))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.dateEdit_2 = QtGui.QDateEdit(self.tab_6)
        self.dateEdit_2.setGeometry(QtCore.QRect(110, 10, 70, 22))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.dateEdit = QtGui.QDateEdit(self.tab_6)
        self.dateEdit.setGeometry(QtCore.QRect(10, 10, 70, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.layers_twidget = QtGui.QTableWidget(self.tab_6)
        self.layers_twidget.setGeometry(QtCore.QRect(10, 40, 361, 241))
        self.layers_twidget.setObjectName(_fromUtf8("layers_twidget"))
        self.layers_twidget.setColumnCount(0)
        self.layers_twidget.setRowCount(0)
        self.filter_view_button = QtGui.QPushButton(self.tab_6)
        self.filter_view_button.setGeometry(QtCore.QRect(287, 290, 75, 23))
        self.filter_view_button.setObjectName(_fromUtf8("filter_view_button"))
        self.filter_chbox = QtGui.QCheckBox(self.tab_6)
        self.filter_chbox.setGeometry(QtCore.QRect(190, 293, 91, 17))
        self.filter_chbox.setObjectName(_fromUtf8("filter_chbox"))
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.au_level2_button_2 = QtGui.QPushButton(self.tab_5)
        self.au_level2_button_2.setGeometry(QtCore.QRect(16, 55, 161, 23))
        self.au_level2_button_2.setObjectName(_fromUtf8("au_level2_button_2"))
        self.au_level1_button_2 = QtGui.QPushButton(self.tab_5)
        self.au_level1_button_2.setGeometry(QtCore.QRect(16, 30, 161, 23))
        self.au_level1_button_2.setObjectName(_fromUtf8("au_level1_button_2"))
        self.layer_view_button_2 = QtGui.QPushButton(self.tab_5)
        self.layer_view_button_2.setGeometry(QtCore.QRect(190, 185, 161, 23))
        self.layer_view_button_2.setStyleSheet(_fromUtf8(""))
        self.layer_view_button_2.setObjectName(_fromUtf8("layer_view_button_2"))
        self.fee_tax_zone_button_2 = QtGui.QPushButton(self.tab_5)
        self.fee_tax_zone_button_2.setGeometry(QtCore.QRect(16, 105, 161, 23))
        self.fee_tax_zone_button_2.setObjectName(_fromUtf8("fee_tax_zone_button_2"))
        self.type_cbox_2 = QtGui.QComboBox(self.tab_5)
        self.type_cbox_2.setGeometry(QtCore.QRect(17, 150, 333, 22))
        self.type_cbox_2.setObjectName(_fromUtf8("type_cbox_2"))
        self.valuation_zone_button_2 = QtGui.QPushButton(self.tab_5)
        self.valuation_zone_button_2.setGeometry(QtCore.QRect(190, 105, 161, 23))
        self.valuation_zone_button_2.setObjectName(_fromUtf8("valuation_zone_button_2"))
        self.sec_zone_button_2 = QtGui.QPushButton(self.tab_5)
        self.sec_zone_button_2.setGeometry(QtCore.QRect(190, 80, 161, 23))
        self.sec_zone_button_2.setObjectName(_fromUtf8("sec_zone_button_2"))
        self.au_level3_button_2 = QtGui.QPushButton(self.tab_5)
        self.au_level3_button_2.setGeometry(QtCore.QRect(16, 80, 161, 23))
        self.au_level3_button_2.setObjectName(_fromUtf8("au_level3_button_2"))
        self.label_2 = QtGui.QLabel(self.tab_5)
        self.label_2.setGeometry(QtCore.QRect(19, 135, 331, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.mpa_zone_button_2 = QtGui.QPushButton(self.tab_5)
        self.mpa_zone_button_2.setGeometry(QtCore.QRect(190, 55, 161, 23))
        self.mpa_zone_button_2.setObjectName(_fromUtf8("mpa_zone_button_2"))
        self.free_zone_button_2 = QtGui.QPushButton(self.tab_5)
        self.free_zone_button_2.setGeometry(QtCore.QRect(190, 30, 161, 23))
        self.free_zone_button_2.setObjectName(_fromUtf8("free_zone_button_2"))
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.tabWidget.addTab(self.st_tm_filter_tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.qa_lwidget = QtGui.QListWidget(self.tab_3)
        self.qa_lwidget.setGeometry(QtCore.QRect(4, 5, 371, 181))
        self.qa_lwidget.setObjectName(_fromUtf8("qa_lwidget"))
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.qa_lwidget.addItem(item)
        self.qa_layer_button = QtGui.QPushButton(self.tab_3)
        self.qa_layer_button.setGeometry(QtCore.QRect(9, 220, 360, 23))
        self.qa_layer_button.setObjectName(_fromUtf8("qa_layer_button"))
        self.p_button = QtGui.QPushButton(self.tab_3)
        self.p_button.setGeometry(QtCore.QRect(90, 250, 201, 23))
        self.p_button.setObjectName(_fromUtf8("p_button"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.maintenance_tab = QtGui.QWidget()
        self.maintenance_tab.setObjectName(_fromUtf8("maintenance_tab"))
        self.groupBox_20 = QtGui.QGroupBox(self.maintenance_tab)
        self.groupBox_20.setGeometry(QtCore.QRect(5, 255, 371, 239))
        self.groupBox_20.setObjectName(_fromUtf8("groupBox_20"))
        self.case_results_twidget = QtGui.QTableWidget(self.groupBox_20)
        self.case_results_twidget.setGeometry(QtCore.QRect(5, 25, 361, 181))
        self.case_results_twidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.case_results_twidget.setObjectName(_fromUtf8("case_results_twidget"))
        self.case_results_twidget.setColumnCount(0)
        self.case_results_twidget.setRowCount(0)
        self.case_finalize_button = QtGui.QPushButton(self.groupBox_20)
        self.case_finalize_button.setGeometry(QtCore.QRect(239, 213, 131, 23))
        self.case_finalize_button.setObjectName(_fromUtf8("case_finalize_button"))
        self.case_revert_button = QtGui.QPushButton(self.groupBox_20)
        self.case_revert_button.setGeometry(QtCore.QRect(115, 213, 111, 23))
        self.case_revert_button.setObjectName(_fromUtf8("case_revert_button"))
        self.case_create_button = QtGui.QPushButton(self.groupBox_20)
        self.case_create_button.setGeometry(QtCore.QRect(0, 213, 101, 23))
        self.case_create_button.setObjectName(_fromUtf8("case_create_button"))
        self.groupBox_21 = QtGui.QGroupBox(self.maintenance_tab)
        self.groupBox_21.setGeometry(QtCore.QRect(5, 0, 371, 256))
        self.groupBox_21.setObjectName(_fromUtf8("groupBox_21"))
        self.case_no_edit = QtGui.QLineEdit(self.groupBox_21)
        self.case_no_edit.setGeometry(QtCore.QRect(10, 28, 170, 20))
        self.case_no_edit.setObjectName(_fromUtf8("case_no_edit"))
        self.case_parcel_no_edit = QtGui.QLineEdit(self.groupBox_21)
        self.case_parcel_no_edit.setGeometry(QtCore.QRect(190, 67, 170, 20))
        self.case_parcel_no_edit.setObjectName(_fromUtf8("case_parcel_no_edit"))
        self.label_50 = QtGui.QLabel(self.groupBox_21)
        self.label_50.setGeometry(QtCore.QRect(10, 13, 170, 17))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_51 = QtGui.QLabel(self.groupBox_21)
        self.label_51.setGeometry(QtCore.QRect(10, 52, 170, 17))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_52 = QtGui.QLabel(self.groupBox_21)
        self.label_52.setGeometry(QtCore.QRect(10, 92, 170, 17))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_53 = QtGui.QLabel(self.groupBox_21)
        self.label_53.setGeometry(QtCore.QRect(190, 13, 170, 17))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.label_54 = QtGui.QLabel(self.groupBox_21)
        self.label_54.setGeometry(QtCore.QRect(190, 52, 170, 16))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.case_completion_date_edit = QtGui.QDateEdit(self.groupBox_21)
        self.case_completion_date_edit.setGeometry(QtCore.QRect(39, 67, 141, 21))
        self.case_completion_date_edit.setCalendarPopup(True)
        self.case_completion_date_edit.setObjectName(_fromUtf8("case_completion_date_edit"))
        self.case_clear_button = QtGui.QPushButton(self.groupBox_21)
        self.case_clear_button.setGeometry(QtCore.QRect(204, 215, 75, 23))
        self.case_clear_button.setObjectName(_fromUtf8("case_clear_button"))
        self.case_find_button = QtGui.QPushButton(self.groupBox_21)
        self.case_find_button.setGeometry(QtCore.QRect(290, 215, 75, 23))
        self.case_find_button.setDefault(True)
        self.case_find_button.setObjectName(_fromUtf8("case_find_button"))
        self.case_completion_date_checkbox = QtGui.QCheckBox(self.groupBox_21)
        self.case_completion_date_checkbox.setGeometry(QtCore.QRect(10, 67, 21, 20))
        self.case_completion_date_checkbox.setText(_fromUtf8(""))
        self.case_completion_date_checkbox.setObjectName(_fromUtf8("case_completion_date_checkbox"))
        self.case_results_label = QtGui.QLabel(self.groupBox_21)
        self.case_results_label.setGeometry(QtCore.QRect(10, 220, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.case_results_label.setFont(font)
        self.case_results_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.case_results_label.setObjectName(_fromUtf8("case_results_label"))
        self.surveyed_by_company_cbox = QtGui.QComboBox(self.groupBox_21)
        self.surveyed_by_company_cbox.setGeometry(QtCore.QRect(9, 107, 171, 21))
        self.surveyed_by_company_cbox.setObjectName(_fromUtf8("surveyed_by_company_cbox"))
        self.surveyed_by_land_officer_cbox = QtGui.QComboBox(self.groupBox_21)
        self.surveyed_by_land_officer_cbox.setGeometry(QtCore.QRect(10, 146, 170, 21))
        self.surveyed_by_land_officer_cbox.setObjectName(_fromUtf8("surveyed_by_land_officer_cbox"))
        self.label_56 = QtGui.QLabel(self.groupBox_21)
        self.label_56.setGeometry(QtCore.QRect(10, 131, 170, 17))
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.finalized_by_cbox = QtGui.QComboBox(self.groupBox_21)
        self.finalized_by_cbox.setGeometry(QtCore.QRect(190, 28, 171, 21))
        self.finalized_by_cbox.setObjectName(_fromUtf8("finalized_by_cbox"))
        self.case_status_cbox = QtGui.QComboBox(self.groupBox_21)
        self.case_status_cbox.setGeometry(QtCore.QRect(190, 146, 170, 21))
        self.case_status_cbox.setObjectName(_fromUtf8("case_status_cbox"))
        self.label_58 = QtGui.QLabel(self.groupBox_21)
        self.label_58.setGeometry(QtCore.QRect(190, 131, 170, 17))
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.label_57 = QtGui.QLabel(self.groupBox_21)
        self.label_57.setGeometry(QtCore.QRect(190, 94, 170, 16))
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.case_app_no_edit = QtGui.QLineEdit(self.groupBox_21)
        self.case_app_no_edit.setGeometry(QtCore.QRect(190, 109, 170, 20))
        self.case_app_no_edit.setObjectName(_fromUtf8("case_app_no_edit"))
        self.personal_case_edit = QtGui.QLineEdit(self.groupBox_21)
        self.personal_case_edit.setGeometry(QtCore.QRect(191, 186, 169, 20))
        self.personal_case_edit.setObjectName(_fromUtf8("personal_case_edit"))
        self.label_81 = QtGui.QLabel(self.groupBox_21)
        self.label_81.setGeometry(QtCore.QRect(193, 173, 153, 10))
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.label_82 = QtGui.QLabel(self.groupBox_21)
        self.label_82.setGeometry(QtCore.QRect(10, 170, 171, 17))
        self.label_82.setObjectName(_fromUtf8("label_82"))
        self.case_right_holder_name_edit = QtGui.QLineEdit(self.groupBox_21)
        self.case_right_holder_name_edit.setGeometry(QtCore.QRect(10, 186, 170, 20))
        self.case_right_holder_name_edit.setObjectName(_fromUtf8("case_right_holder_name_edit"))
        self.tabWidget.addTab(self.maintenance_tab, _fromUtf8(""))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        PlanNavigatorWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(PlanNavigatorWidget)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PlanNavigatorWidget)
        PlanNavigatorWidget.setTabOrder(self.tabWidget, self.extent_rbutton)
        PlanNavigatorWidget.setTabOrder(self.extent_rbutton, self.get_extent_button)
        PlanNavigatorWidget.setTabOrder(self.get_extent_button, self.extent_west_spinbox)
        PlanNavigatorWidget.setTabOrder(self.extent_west_spinbox, self.extent_east_spinbox)
        PlanNavigatorWidget.setTabOrder(self.extent_east_spinbox, self.extent_north_spinbox)
        PlanNavigatorWidget.setTabOrder(self.extent_north_spinbox, self.extent_south_spinbox)
        PlanNavigatorWidget.setTabOrder(self.extent_south_spinbox, self.apply_button)
        PlanNavigatorWidget.setTabOrder(self.apply_button, self.remove_button)
        PlanNavigatorWidget.setTabOrder(self.remove_button, self.clear_b_box_button)
        PlanNavigatorWidget.setTabOrder(self.clear_b_box_button, self.from_date_edit)
        PlanNavigatorWidget.setTabOrder(self.from_date_edit, self.till_date_edit)
        PlanNavigatorWidget.setTabOrder(self.till_date_edit, self.infinity_check_box)
        PlanNavigatorWidget.setTabOrder(self.infinity_check_box, self.temp_filter_apply_button)
        PlanNavigatorWidget.setTabOrder(self.temp_filter_apply_button, self.status_cbox)
        PlanNavigatorWidget.setTabOrder(self.status_cbox, self.office_in_charge_cbox)
        PlanNavigatorWidget.setTabOrder(self.office_in_charge_cbox, self.plan_num_edit)
        PlanNavigatorWidget.setTabOrder(self.plan_num_edit, self.plan_clear_button)
        PlanNavigatorWidget.setTabOrder(self.plan_clear_button, self.plan_find_button)
        PlanNavigatorWidget.setTabOrder(self.plan_find_button, self.plan_results_twidget)
        PlanNavigatorWidget.setTabOrder(self.plan_results_twidget, self.case_button)
        PlanNavigatorWidget.setTabOrder(self.case_button, self.plan_edit_button)
        PlanNavigatorWidget.setTabOrder(self.plan_edit_button, self.current_view_button)
        PlanNavigatorWidget.setTabOrder(self.current_view_button, self.case_no_edit)
        PlanNavigatorWidget.setTabOrder(self.case_no_edit, self.case_completion_date_checkbox)
        PlanNavigatorWidget.setTabOrder(self.case_completion_date_checkbox, self.case_completion_date_edit)
        PlanNavigatorWidget.setTabOrder(self.case_completion_date_edit, self.surveyed_by_company_cbox)
        PlanNavigatorWidget.setTabOrder(self.surveyed_by_company_cbox, self.surveyed_by_land_officer_cbox)
        PlanNavigatorWidget.setTabOrder(self.surveyed_by_land_officer_cbox, self.finalized_by_cbox)
        PlanNavigatorWidget.setTabOrder(self.finalized_by_cbox, self.case_parcel_no_edit)
        PlanNavigatorWidget.setTabOrder(self.case_parcel_no_edit, self.case_status_cbox)
        PlanNavigatorWidget.setTabOrder(self.case_status_cbox, self.case_clear_button)
        PlanNavigatorWidget.setTabOrder(self.case_clear_button, self.case_find_button)
        PlanNavigatorWidget.setTabOrder(self.case_find_button, self.case_results_twidget)
        PlanNavigatorWidget.setTabOrder(self.case_results_twidget, self.case_create_button)
        PlanNavigatorWidget.setTabOrder(self.case_create_button, self.case_revert_button)
        PlanNavigatorWidget.setTabOrder(self.case_revert_button, self.case_finalize_button)
        PlanNavigatorWidget.setTabOrder(self.case_finalize_button, self.scrollArea)

    def retranslateUi(self, PlanNavigatorWidget):
        PlanNavigatorWidget.setWindowTitle(_translate("PlanNavigatorWidget", "Selection / Filter", None))
        self.groupBox_11.setTitle(_translate("PlanNavigatorWidget", "Criteria", None))
        self.label_31.setText(_translate("PlanNavigatorWidget", "Status", None))
        self.label_32.setText(_translate("PlanNavigatorWidget", "Officer In Charge", None))
        self.label_34.setText(_translate("PlanNavigatorWidget", "Draft No", None))
        self.plan_results_label.setText(_translate("PlanNavigatorWidget", "Results:", None))
        self.label_37.setText(_translate("PlanNavigatorWidget", "Next Officer In Charge", None))
        self.label_55.setText(_translate("PlanNavigatorWidget", "Plan Type", None))
        self.plan_date_checkbox.setText(_translate("PlanNavigatorWidget", "Date", None))
        self.label_33.setText(_translate("PlanNavigatorWidget", "Decision Level", None))
        self.plan_find_button.setText(_translate("PlanNavigatorWidget", "Find", None))
        self.plan_clear_button.setText(_translate("PlanNavigatorWidget", "Clear", None))
        self.groupBox_12.setTitle(_translate("PlanNavigatorWidget", "Results", None))
        self.current_view_button.setText(_translate("PlanNavigatorWidget", "LayerView", None))
        self.plan_edit_button.setText(_translate("PlanNavigatorWidget", "Edit", None))
        self.case_button.setText(_translate("PlanNavigatorWidget", "Create Case", None))
        self.is_filter_chbox.setText(_translate("PlanNavigatorWidget", "Is Filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plan_tab), _translate("PlanNavigatorWidget", "Land Plan", None))
        self.spatial_groupbox.setTitle(_translate("PlanNavigatorWidget", "Spatial Filter", None))
        self.get_extent_button.setText(_translate("PlanNavigatorWidget", "Get Extent", None))
        self.apply_button.setText(_translate("PlanNavigatorWidget", "Apply", None))
        self.clear_b_box_button.setText(_translate("PlanNavigatorWidget", "Clear BBox", None))
        self.remove_button.setText(_translate("PlanNavigatorWidget", "Remove", None))
        self.extent_rbutton.setText(_translate("PlanNavigatorWidget", "Extent", None))
        self.groupBox_6.setTitle(_translate("PlanNavigatorWidget", "Temporal Filter", None))
        self.from_date_edit.setDisplayFormat(_translate("PlanNavigatorWidget", "yyyy-MM-dd", None))
        self.till_date_edit.setDisplayFormat(_translate("PlanNavigatorWidget", "yyyy-MM-dd", None))
        self.infinity_check_box.setText(_translate("PlanNavigatorWidget", "Infinity", None))
        self.temp_filter_apply_button.setText(_translate("PlanNavigatorWidget", "Apply", None))
        self.label_12.setText(_translate("PlanNavigatorWidget", "From", None))
        self.filter_view_button.setText(_translate("PlanNavigatorWidget", "View", None))
        self.filter_chbox.setText(_translate("PlanNavigatorWidget", "Is Filter", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("PlanNavigatorWidget", "Base Layer", None))
        self.au_level2_button_2.setText(_translate("PlanNavigatorWidget", "Сум/Дүүргийн хил", None))
        self.au_level1_button_2.setText(_translate("PlanNavigatorWidget", "Аймаг/Нийслэлийн хил", None))
        self.layer_view_button_2.setText(_translate("PlanNavigatorWidget", "layer view", None))
        self.fee_tax_zone_button_2.setText(_translate("PlanNavigatorWidget", "Төлбөр, Татварын бүс", None))
        self.valuation_zone_button_2.setText(_translate("PlanNavigatorWidget", "Үнэлгээний бүс", None))
        self.sec_zone_button_2.setText(_translate("PlanNavigatorWidget", "Хамгаалалтын зурвас", None))
        self.au_level3_button_2.setText(_translate("PlanNavigatorWidget", "Баг/Хорооны хил", None))
        self.label_2.setText(_translate("PlanNavigatorWidget", "Type", None))
        self.mpa_zone_button_2.setText(_translate("PlanNavigatorWidget", "Тусгай хамгаалалтай газар", None))
        self.free_zone_button_2.setText(_translate("PlanNavigatorWidget", "Чөлөөт бүс", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("PlanNavigatorWidget", "Other Layer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.st_tm_filter_tab), _translate("PlanNavigatorWidget", "ST/TM Filter", None))
        __sortingEnabled = self.qa_lwidget.isSortingEnabled()
        self.qa_lwidget.setSortingEnabled(False)
        item = self.qa_lwidget.item(0)
        item.setText(_translate("PlanNavigatorWidget", "01.Building overlapping parcels", None))
        item = self.qa_lwidget.item(1)
        item.setText(_translate("PlanNavigatorWidget", "02.Overlapping buildings", None))
        item = self.qa_lwidget.item(2)
        item.setText(_translate("PlanNavigatorWidget", "03.Overlapping parcels", None))
        item = self.qa_lwidget.item(3)
        item.setText(_translate("PlanNavigatorWidget", "04.Parcels overlapping buildings", None))
        item = self.qa_lwidget.item(4)
        item.setText(_translate("PlanNavigatorWidget", "05.Parcels overlapping fee zones", None))
        item = self.qa_lwidget.item(5)
        item.setText(_translate("PlanNavigatorWidget", "06.Parcels without buildings", None))
        item = self.qa_lwidget.item(6)
        item.setText(_translate("PlanNavigatorWidget", "07.Incorrect street names", None))
        item = self.qa_lwidget.item(7)
        item.setText(_translate("PlanNavigatorWidget", "08.Incorrect khashaa number", None))
        item = self.qa_lwidget.item(8)
        item.setText(_translate("PlanNavigatorWidget", "09.Parcel Info Statistic", None))
        self.qa_lwidget.setSortingEnabled(__sortingEnabled)
        self.qa_layer_button.setText(_translate("PlanNavigatorWidget", "Layer View", None))
        self.p_button.setText(_translate("PlanNavigatorWidget", "print", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PlanNavigatorWidget", "Quality Check", None))
        self.groupBox_20.setTitle(_translate("PlanNavigatorWidget", "Results", None))
        self.case_finalize_button.setText(_translate("PlanNavigatorWidget", "Finalize Case", None))
        self.case_revert_button.setText(_translate("PlanNavigatorWidget", "Revert Case", None))
        self.case_create_button.setText(_translate("PlanNavigatorWidget", "Create Case", None))
        self.groupBox_21.setTitle(_translate("PlanNavigatorWidget", "Criteria", None))
        self.label_50.setText(_translate("PlanNavigatorWidget", "Case Number", None))
        self.label_51.setText(_translate("PlanNavigatorWidget", "Completion Date", None))
        self.label_52.setText(_translate("PlanNavigatorWidget", "Surveyed By Company", None))
        self.label_53.setText(_translate("PlanNavigatorWidget", "Finalized By", None))
        self.label_54.setText(_translate("PlanNavigatorWidget", "Parcel Number", None))
        self.case_completion_date_edit.setDisplayFormat(_translate("PlanNavigatorWidget", "yyyy-MM-dd", None))
        self.case_clear_button.setText(_translate("PlanNavigatorWidget", "Clear", None))
        self.case_find_button.setText(_translate("PlanNavigatorWidget", "Find", None))
        self.case_results_label.setText(_translate("PlanNavigatorWidget", "Results:", None))
        self.label_56.setText(_translate("PlanNavigatorWidget", "Surveyed By Land Officer", None))
        self.label_58.setText(_translate("PlanNavigatorWidget", "Case Status", None))
        self.label_57.setText(_translate("PlanNavigatorWidget", "Application Number", None))
        self.label_81.setText(_translate("PlanNavigatorWidget", "Personal / Company ID", None))
        self.label_82.setText(_translate("PlanNavigatorWidget", "Right Holder Name", None))
        self.case_right_holder_name_edit.setToolTip(_translate("PlanNavigatorWidget", "insert a comma to search for first and surname: surname, first_name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maintenance_tab), _translate("PlanNavigatorWidget", "Maitenance Case", None))

