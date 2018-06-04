# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacherMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_teacher_MainWindow(object):
    def setupUi(self, teacher_MainWindow):
        teacher_MainWindow.setObjectName("teacher_MainWindow")
        teacher_MainWindow.resize(1368, 768)
        self.centralwidget = QtWidgets.QWidget(teacher_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.user_top_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_top_label.sizePolicy().hasHeightForWidth())
        self.user_top_label.setSizePolicy(sizePolicy)
        self.user_top_label.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.user_top_label.setObjectName("user_top_label")
        self.horizontalLayout.addWidget(self.user_top_label)
        self.logout_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_button.sizePolicy().hasHeightForWidth())
        self.logout_button.setSizePolicy(sizePolicy)
        self.logout_button.setMaximumSize(QtCore.QSize(85, 16777215))
        self.logout_button.setStyleSheet("")
        self.logout_button.setIconSize(QtCore.QSize(20, 20))
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabBar::tab:first { height: 45px;}")
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.home_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.welcome_label = QtWidgets.QLabel(self.home_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.welcome_label.sizePolicy().hasHeightForWidth())
        self.welcome_label.setSizePolicy(sizePolicy)
        self.welcome_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout_2.addWidget(self.welcome_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.last_login_label = QtWidgets.QLabel(self.home_tab)
        self.last_login_label.setStyleSheet("font: 12pt \"Sans Serif\";\n"
"margin-right: 10px;")
        self.last_login_label.setObjectName("last_login_label")
        self.verticalLayout_2.addWidget(self.last_login_label, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.tabWidget.addTab(self.home_tab, "")
        self.query_tab = QtWidgets.QWidget()
        self.query_tab.setObjectName("query_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.query_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.query_tab)
        self.tabWidget_2.setStyleSheet("QTabBar::tab { height: 45px}")
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.courses_tab = QtWidgets.QWidget()
        self.courses_tab.setObjectName("courses_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.courses_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_21 = QtWidgets.QLabel(self.courses_tab)
        self.label_21.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)
        self.course_year_comboBox = QtWidgets.QComboBox(self.courses_tab)
        self.course_year_comboBox.setEnabled(True)
        self.course_year_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_year_comboBox.setObjectName("course_year_comboBox")
        self.course_year_comboBox.addItem("")
        self.course_year_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.course_year_comboBox)
        self.label_22 = QtWidgets.QLabel(self.courses_tab)
        self.label_22.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_8.addWidget(self.label_22)
        self.course_semester_comboBox = QtWidgets.QComboBox(self.courses_tab)
        self.course_semester_comboBox.setEnabled(True)
        self.course_semester_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_semester_comboBox.setObjectName("course_semester_comboBox")
        self.course_semester_comboBox.addItem("")
        self.course_semester_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.course_semester_comboBox)
        self.label = QtWidgets.QLabel(self.courses_tab)
        self.label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.course_name_comboBox = QtWidgets.QComboBox(self.courses_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_name_comboBox.sizePolicy().hasHeightForWidth())
        self.course_name_comboBox.setSizePolicy(sizePolicy)
        self.course_name_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_name_comboBox.setObjectName("course_name_comboBox")
        self.course_name_comboBox.addItem("")
        self.course_name_comboBox.addItem("")
        self.course_name_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.course_name_comboBox)
        self.course_query_button = QtWidgets.QPushButton(self.courses_tab)
        self.course_query_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_query_button.setObjectName("course_query_button")
        self.horizontalLayout_8.addWidget(self.course_query_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.line_12 = QtWidgets.QFrame(self.courses_tab)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_3.addWidget(self.line_12)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.course_id_label = QtWidgets.QLabel(self.courses_tab)
        self.course_id_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_id_label.setObjectName("course_id_label")
        self.gridLayout_2.addWidget(self.course_id_label, 0, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.courses_tab)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 0, 1, 1, 1)
        self.teacher_label = QtWidgets.QLabel(self.courses_tab)
        self.teacher_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.teacher_label.setObjectName("teacher_label")
        self.gridLayout_2.addWidget(self.teacher_label, 0, 2, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.courses_tab)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 0, 3, 1, 1)
        self.class_time_label = QtWidgets.QLabel(self.courses_tab)
        self.class_time_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.class_time_label.setObjectName("class_time_label")
        self.gridLayout_2.addWidget(self.class_time_label, 0, 4, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.courses_tab)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 1, 0, 2, 3)
        self.line_9 = QtWidgets.QFrame(self.courses_tab)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 1, 4, 1, 1)
        self.school_label = QtWidgets.QLabel(self.courses_tab)
        self.school_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.school_label.setObjectName("school_label")
        self.gridLayout_2.addWidget(self.school_label, 2, 4, 2, 1)
        self.location_label = QtWidgets.QLabel(self.courses_tab)
        self.location_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.location_label.setObjectName("location_label")
        self.gridLayout_2.addWidget(self.location_label, 3, 0, 1, 3)
        self.line_11 = QtWidgets.QFrame(self.courses_tab)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_2.addWidget(self.line_11, 3, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.course_tableWidget = QtWidgets.QTableWidget(self.courses_tab)
        self.course_tableWidget.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.course_tableWidget.setObjectName("course_tableWidget")
        self.course_tableWidget.setColumnCount(6)
        self.course_tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_tableWidget.setItem(0, 4, item)
        self.verticalLayout_3.addWidget(self.course_tableWidget)
        self.confirm_grade_button = QtWidgets.QPushButton(self.courses_tab)
        self.confirm_grade_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.confirm_grade_button.setObjectName("confirm_grade_button")
        self.verticalLayout_3.addWidget(self.confirm_grade_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.print_button = QtWidgets.QPushButton(self.courses_tab)
        self.print_button.setMinimumSize(QtCore.QSize(130, 0))
        self.print_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.print_button.setObjectName("print_button")
        self.horizontalLayout_2.addWidget(self.print_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.grade_analysis_button = QtWidgets.QPushButton(self.courses_tab)
        self.grade_analysis_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.grade_analysis_button.setObjectName("grade_analysis_button")
        self.horizontalLayout_2.addWidget(self.grade_analysis_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget_2.addTab(self.courses_tab, "")
        self.exam_tab = QtWidgets.QWidget()
        self.exam_tab.setObjectName("exam_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.exam_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.exam_tab)
        self.label_18.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.comboBox_6 = QtWidgets.QComboBox(self.exam_tab)
        self.comboBox_6.setEnabled(True)
        self.comboBox_6.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_6)
        self.label_19 = QtWidgets.QLabel(self.exam_tab)
        self.label_19.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        self.comboBox_7 = QtWidgets.QComboBox(self.exam_tab)
        self.comboBox_7.setEnabled(True)
        self.comboBox_7.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_7)
        self.label_20 = QtWidgets.QLabel(self.exam_tab)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_6.addWidget(self.label_20)
        self.pushButton_5 = QtWidgets.QPushButton(self.exam_tab)
        self.pushButton_5.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.exam_tab)
        self.tableWidget_4.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.verticalLayout_7.addWidget(self.tableWidget_4)
        self.tabWidget_2.addTab(self.exam_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_10.addWidget(self.label_25)
        self.comboBox_12 = QtWidgets.QComboBox(self.tab)
        self.comboBox_12.setEnabled(True)
        self.comboBox_12.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_12)
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        self.comboBox_13 = QtWidgets.QComboBox(self.tab)
        self.comboBox_13.setEnabled(True)
        self.comboBox_13.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_13)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_10.addWidget(self.pushButton_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_6.setSizePolicy(sizePolicy)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(1, 0, item)
        self.horizontalLayout_12.addWidget(self.tableWidget_6)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_9.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget_2.addTab(self.tab, "")
        self.personal_info_tab = QtWidgets.QWidget()
        self.personal_info_tab.setObjectName("personal_info_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.personal_info_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.personal_info_tab)
        self.tableWidget_5.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(4)
        self.tableWidget_5.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(6, 2, item)
        self.verticalLayout_8.addWidget(self.tableWidget_5)
        self.tabWidget_2.addTab(self.personal_info_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.query_tab, "")
        self.change_pw_tab = QtWidgets.QWidget()
        self.change_pw_tab.setObjectName("change_pw_tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.change_pw_tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_10.addItem(spacerItem9)
        self.old_password_line_edit = QtWidgets.QLineEdit(self.change_pw_tab)
        self.old_password_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.old_password_line_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.old_password_line_edit.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.old_password_line_edit.setInputMask("")
        self.old_password_line_edit.setText("")
        self.old_password_line_edit.setObjectName("old_password_line_edit")
        self.verticalLayout_10.addWidget(self.old_password_line_edit, 0, QtCore.Qt.AlignHCenter)
        self.new_password_line_edit = QtWidgets.QLineEdit(self.change_pw_tab)
        self.new_password_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.new_password_line_edit.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.new_password_line_edit.setObjectName("new_password_line_edit")
        self.verticalLayout_10.addWidget(self.new_password_line_edit, 0, QtCore.Qt.AlignHCenter)
        self.confirm_password_line_edit = QtWidgets.QLineEdit(self.change_pw_tab)
        self.confirm_password_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.confirm_password_line_edit.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.confirm_password_line_edit.setObjectName("confirm_password_line_edit")
        self.verticalLayout_10.addWidget(self.confirm_password_line_edit, 0, QtCore.Qt.AlignHCenter)
        self.change_password_button = QtWidgets.QPushButton(self.change_pw_tab)
        self.change_password_button.setMinimumSize(QtCore.QSize(100, 0))
        self.change_password_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.change_password_button.setObjectName("change_password_button")
        self.verticalLayout_10.addWidget(self.change_password_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem10)
        self.tabWidget.addTab(self.change_pw_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        teacher_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(teacher_MainWindow)
        self.statusbar.setObjectName("statusbar")
        teacher_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(teacher_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(teacher_MainWindow)

    def retranslateUi(self, teacher_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        teacher_MainWindow.setWindowTitle(_translate("teacher_MainWindow", "Course Management System"))
        self.user_top_label.setText(_translate("teacher_MainWindow", "2015329620057 HP."))
        self.logout_button.setText(_translate("teacher_MainWindow", "Logout"))
        self.welcome_label.setText(_translate("teacher_MainWindow", "Welcome, 20031111 HP"))
        self.last_login_label.setText(_translate("teacher_MainWindow", "Last login: 2018-XX-XX 12:00 Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("teacher_MainWindow", "Home"))
        self.label_21.setText(_translate("teacher_MainWindow", "Year:"))
        self.course_year_comboBox.setItemText(0, _translate("teacher_MainWindow", "2015-2016"))
        self.course_year_comboBox.setItemText(1, _translate("teacher_MainWindow", "2016-2017"))
        self.label_22.setText(_translate("teacher_MainWindow", "Semester:"))
        self.course_semester_comboBox.setItemText(0, _translate("teacher_MainWindow", "1"))
        self.course_semester_comboBox.setItemText(1, _translate("teacher_MainWindow", "2"))
        self.label.setText(_translate("teacher_MainWindow", "My Courses:"))
        self.course_name_comboBox.setItemText(0, _translate("teacher_MainWindow", "Java"))
        self.course_name_comboBox.setItemText(1, _translate("teacher_MainWindow", "C++ GUI Programming"))
        self.course_name_comboBox.setItemText(2, _translate("teacher_MainWindow", "Data Structures and Algorithms"))
        self.course_query_button.setText(_translate("teacher_MainWindow", "Query"))
        self.course_id_label.setText(_translate("teacher_MainWindow", "Course ID: 666"))
        self.teacher_label.setText(_translate("teacher_MainWindow", "Teacher Name: zf"))
        self.class_time_label.setText(_translate("teacher_MainWindow", "Class Time: Monday 8:10-9:45"))
        self.school_label.setText(_translate("teacher_MainWindow", "School: shit"))
        self.location_label.setText(_translate("teacher_MainWindow", "Location: fuck"))
        item = self.course_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "1"))
        item = self.course_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "Student Name"))
        item = self.course_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("teacher_MainWindow", "Student ID"))
        item = self.course_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("teacher_MainWindow", "School"))
        item = self.course_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("teacher_MainWindow", "Classs"))
        item = self.course_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("teacher_MainWindow", "Phone Number"))
        item = self.course_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("teacher_MainWindow", "Grade"))
        __sortingEnabled = self.course_tableWidget.isSortingEnabled()
        self.course_tableWidget.setSortingEnabled(False)
        item = self.course_tableWidget.item(0, 0)
        item.setText(_translate("teacher_MainWindow", "Bob"))
        item = self.course_tableWidget.item(0, 1)
        item.setText(_translate("teacher_MainWindow", "201123415"))
        item = self.course_tableWidget.item(0, 2)
        item.setText(_translate("teacher_MainWindow", "Information"))
        item = self.course_tableWidget.item(0, 3)
        item.setText(_translate("teacher_MainWindow", "   CS15(1)"))
        item = self.course_tableWidget.item(0, 4)
        item.setText(_translate("teacher_MainWindow", "66666666"))
        self.course_tableWidget.setSortingEnabled(__sortingEnabled)
        self.confirm_grade_button.setText(_translate("teacher_MainWindow", "Confirm Grades"))
        self.print_button.setText(_translate("teacher_MainWindow", "Print"))
        self.grade_analysis_button.setText(_translate("teacher_MainWindow", "Grades Analysis"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.courses_tab), _translate("teacher_MainWindow", "My Courses"))
        self.label_18.setText(_translate("teacher_MainWindow", "Year:"))
        self.comboBox_6.setItemText(0, _translate("teacher_MainWindow", "2015-2016"))
        self.comboBox_6.setItemText(1, _translate("teacher_MainWindow", "2016-2017"))
        self.label_19.setText(_translate("teacher_MainWindow", "Semester:"))
        self.comboBox_7.setItemText(0, _translate("teacher_MainWindow", "1"))
        self.comboBox_7.setItemText(1, _translate("teacher_MainWindow", "2"))
        self.pushButton_5.setText(_translate("teacher_MainWindow", "Query"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "Course ID"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("teacher_MainWindow", "Course Name"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("teacher_MainWindow", "Exam TIme"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("teacher_MainWindow", "Exam Location"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.exam_tab), _translate("teacher_MainWindow", "Exam Query"))
        self.label_25.setText(_translate("teacher_MainWindow", "Year:"))
        self.comboBox_12.setItemText(0, _translate("teacher_MainWindow", "2015-2016"))
        self.comboBox_12.setItemText(1, _translate("teacher_MainWindow", "2016-2017"))
        self.label_26.setText(_translate("teacher_MainWindow", "Semester:"))
        self.comboBox_13.setItemText(0, _translate("teacher_MainWindow", "1"))
        self.comboBox_13.setItemText(1, _translate("teacher_MainWindow", "2"))
        self.pushButton_8.setText(_translate("teacher_MainWindow", "Show Courses"))
        self.label_4.setText(_translate("teacher_MainWindow", "My Courses:"))
        self.comboBox_3.setItemText(0, _translate("teacher_MainWindow", "Java"))
        self.comboBox_3.setItemText(1, _translate("teacher_MainWindow", "C++ GUI Programming"))
        self.comboBox_3.setItemText(2, _translate("teacher_MainWindow", "Data Structures and Algorithms"))
        self.tableWidget_6.setSortingEnabled(True)
        item = self.tableWidget_6.verticalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "1"))
        item = self.tableWidget_6.verticalHeaderItem(1)
        item.setText(_translate("teacher_MainWindow", "2"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "Grade"))
        __sortingEnabled = self.tableWidget_6.isSortingEnabled()
        self.tableWidget_6.setSortingEnabled(False)
        item = self.tableWidget_6.item(0, 0)
        item.setText(_translate("teacher_MainWindow", "85"))
        item = self.tableWidget_6.item(1, 0)
        item.setText(_translate("teacher_MainWindow", "88"))
        self.tableWidget_6.setSortingEnabled(__sortingEnabled)
        self.pushButton_9.setText(_translate("teacher_MainWindow", "Data Analysis"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("teacher_MainWindow", " My Courses Evaluation"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(3)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(4)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(5)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(6)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.item(0, 0)
        item.setText(_translate("teacher_MainWindow", "Teacher ID:"))
        item = self.tableWidget_5.item(0, 2)
        item.setText(_translate("teacher_MainWindow", "School:"))
        item = self.tableWidget_5.item(1, 0)
        item.setText(_translate("teacher_MainWindow", "Name:"))
        item = self.tableWidget_5.item(1, 2)
        item.setText(_translate("teacher_MainWindow", "Department:"))
        item = self.tableWidget_5.item(2, 0)
        item.setText(_translate("teacher_MainWindow", "Gender:"))
        item = self.tableWidget_5.item(2, 2)
        item.setText(_translate("teacher_MainWindow", "Position:"))
        item = self.tableWidget_5.item(3, 0)
        item.setText(_translate("teacher_MainWindow", "Birth Date:"))
        item = self.tableWidget_5.item(3, 2)
        item.setText(_translate("teacher_MainWindow", "Phone No.:"))
        item = self.tableWidget_5.item(4, 0)
        item.setText(_translate("teacher_MainWindow", "Folk:"))
        item = self.tableWidget_5.item(5, 0)
        item.setText(_translate("teacher_MainWindow", "Hometown:"))
        item = self.tableWidget_5.item(6, 0)
        item.setText(_translate("teacher_MainWindow", "Political Status:"))
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.personal_info_tab), _translate("teacher_MainWindow", "Personal Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.query_tab), _translate("teacher_MainWindow", "Information Query"))
        self.old_password_line_edit.setPlaceholderText(_translate("teacher_MainWindow", "Old Password"))
        self.new_password_line_edit.setPlaceholderText(_translate("teacher_MainWindow", "New Password"))
        self.confirm_password_line_edit.setPlaceholderText(_translate("teacher_MainWindow", "Confirm Password"))
        self.change_password_button.setText(_translate("teacher_MainWindow", "Change"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.change_pw_tab), _translate("teacher_MainWindow", "Change Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    teacher_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_teacher_MainWindow()
    ui.setupUi(teacher_MainWindow)
    teacher_MainWindow.show()
    sys.exit(app.exec_())

