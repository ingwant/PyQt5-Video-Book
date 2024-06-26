# Form implementation generated from reading ui file '.\new_main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 727)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QToolBox::tab,\n"
"QPushButton,\n"
"QLabel,\n"
"QPlainTextEdit,\n"
"QRadioButton,\n"
"QStatusBar\n"
"{\n"
"    font-family: system-ui;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#title_frame {\n"
" background-color: #393e4d;\n"
"\n"
"}\n"
"\n"
"#title_frame QLabel {\n"
"    font-family: Zurich XBlk BT;\n"
"    font-size: 30px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QToolBoxButton {\n"
"    min-height: 35px;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #a6a29a, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.6 #D8D8D8, stop: 1.0 #a6a29a);\n"
"\n"
"    padding: 0 10px ;\n"
"    \n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLabel {\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-color:#0a3622;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox,\n"
"QSpinBox,\n"
"QLineEdit {\n"
"    min-height: 20px;\n"
"    padding: 5px;\n"
"   font-family: Segoe UI Semibold;\n"
"    font-size: 14px;\n"
"    color: #3232CD;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    padding: 10px;\n"
"    border-top-right-radius: 10px 15px; \n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 10px 15px;\n"
"    border-bottom-right-radius: 5px;\n"
"    max-width: 200px;\n"
"    background-color: #2d6df4;\n"
"    font-weight: 300;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #b0ada6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2050b0;\n"
"}\n"
"\n"
"\n"
"#db_frame {\n"
"    background-color: #fff;\n"
"    border: 1px solid #f8f9fa;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#db_frame QLabel {\n"
"    background-color: #d4e6de;\n"
"    max-width: 150px;\n"
"}\n"
"\n"
"#info_frame QLabel {\n"
"    background-color: #d2e1fc;\n"
"    color: #000;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#info_frame QLineEdit {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"#question_frame QLabel {\n"
"    background-color: #ffc107;\n"
"    color: #000;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"\n"
"#answer_frame {\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.toolBox = QtWidgets.QToolBox(parent=self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 987, 510))
        self.page.setObjectName("page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.db_frame = QtWidgets.QFrame(parent=self.page)
        self.db_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.db_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.db_frame.setObjectName("db_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.db_frame)
        self.gridLayout_2.setContentsMargins(15, 20, 15, -1)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.db_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.db_frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.db_frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.db_frame)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_2.addWidget(self.comboBox_5, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.db_frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.db_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(-1, 20, -1, 15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icons/search-9-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 4)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.db_frame)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(50)
        self.spinBox_2.setProperty("value", 50)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 0, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.db_frame)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 1, 3, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.db_frame)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_2.addWidget(self.comboBox_6, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.db_frame, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 1, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\icons/settings-9-64 (1).ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.page, icon2, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 987, 510))
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        self.questions_frame = QtWidgets.QFrame(parent=self.page_2)
        self.questions_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.questions_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.questions_frame.setObjectName("questions_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.questions_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_frame = QtWidgets.QFrame(parent=self.questions_frame)
        self.info_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_frame.setObjectName("info_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.info_frame)
        self.gridLayout_4.setHorizontalSpacing(30)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.question_count_label = QtWidgets.QLabel(parent=self.info_frame)
        self.question_count_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.question_count_label.setObjectName("question_count_label")
        self.gridLayout_4.addWidget(self.question_count_label, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.info_frame)
        self.question_frame = QtWidgets.QFrame(parent=self.questions_frame)
        self.question_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.question_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.question_frame.setObjectName("question_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.question_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(parent=self.question_frame)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.question_frame)
        self.plainTextEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("system-ui")
        font.setPointSize(-1)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: #fff;\n"
"color: #000;\n"
"padding: 5px 10px;")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.answer_frame = QtWidgets.QFrame(parent=self.question_frame)
        self.answer_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.answer_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.answer_frame.setObjectName("answer_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.answer_frame)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.answer_frame)
        self.verticalLayout_3.addWidget(self.question_frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.function_frame = QtWidgets.QFrame(parent=self.questions_frame)
        self.function_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.function_frame.setObjectName("function_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.function_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.function_frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\icons/refresh-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.function_frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\icons/checkmark-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.function_frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\icons/arrow-21-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.function_frame)
        self.gridLayout.addWidget(self.questions_frame, 0, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\icons/question-mark-64.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.page_2, icon6, "")
        self.gridLayout_5.addWidget(self.toolBox, 1, 0, 1, 1)
        self.title_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.title_frame.setStyleSheet("")
        self.title_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_frame.setObjectName("title_frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.title_frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.title_frame)
        font = QtGui.QFont()
        font.setFamily("Zurich XBlk BT")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.title_frame)
        self.label.setMaximumSize(QtCore.QSize(100, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\icons/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 0, 3, 1, 1)
        self.gridLayout_5.addWidget(self.title_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quiz Application"))
        self.label_3.setText(_translate("MainWindow", "Select Category"))
        self.label_11.setText(_translate("MainWindow", "Number of Questions"))
        self.label_7.setText(_translate("MainWindow", "Select Difficulty"))
        self.label_9.setText(_translate("MainWindow", "Select Type"))
        self.pushButton_5.setText(_translate("MainWindow", "Get New Questions"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Settings"))
        self.label_6.setText(_translate("MainWindow", "Category"))
        self.label_8.setText(_translate("MainWindow", "difficulty"))
        self.question_count_label.setText(_translate("MainWindow", "10/50"))
        self.label_10.setText(_translate("MainWindow", "Question:"))
        self.pushButton_3.setText(_translate("MainWindow", "Try Again"))
        self.pushButton_4.setText(_translate("MainWindow", "Check"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Questions"))
        self.label_2.setText(_translate("MainWindow", "Quiz Application"))
