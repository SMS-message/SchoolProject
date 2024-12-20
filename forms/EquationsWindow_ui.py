# Form implementation generated from reading ui file 'EquationsWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Equation(object):
    def setupUi(self, Equation):
        Equation.setObjectName("Equation")
        Equation.resize(630, 481)
        Equation.setMinimumSize(QtCore.QSize(630, 0))
        Equation.setMaximumSize(QtCore.QSize(630, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        Equation.setFont(font)
        Equation.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    \n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"\n"
"    width: 300px;\n"
"    height: 20px;\n"
"    \n"
"    border: solid;\n"
"    border-color: #353535;\n"
"    border-width: 1px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: rgb(170, 170, 170);\n"
"    border-width: 2px;\n"
"\n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    \n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(Equation)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.returnBtn = QtWidgets.QPushButton(parent=Equation)
        self.returnBtn.setObjectName("returnBtn")
        self.gridLayout_3.addWidget(self.returnBtn, 2, 1, 1, 1)
        self.runBtn = QtWidgets.QPushButton(parent=Equation)
        self.runBtn.setStyleSheet("")
        self.runBtn.setObjectName("runBtn")
        self.gridLayout_3.addWidget(self.runBtn, 1, 1, 1, 1)
        self.EquationTabs = QtWidgets.QTabWidget(parent=Equation)
        self.EquationTabs.setStyleSheet("QLineEdit {\n"
"    padding: 2px; \n"
"    background-color: rgb(20, 20, 20);\n"
"    border: solid;\n"
"    border-color: #353535;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"    border-top: 1px solid #353535;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    padding: 1px 1px 1px 1px;\n"
"    font-family: open sans;    \n"
"\n"
"    height: 20px;\n"
"    border: solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"}\n"
"\n"
"   ")
        self.EquationTabs.setObjectName("EquationTabs")
        self.linEq = QtWidgets.QWidget()
        self.linEq.setObjectName("linEq")
        self.label = QtWidgets.QLabel(parent=self.linEq)
        self.label.setGeometry(QtCore.QRect(10, 10, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    border: dashed;\n"
"    border-width: 2px;\n"
"    border-color: #CCCCCC;\n"
"    border-radius: 5px;\n"
"}")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.linEq)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 581, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 1, 1, 1)
        self.kEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kEdit.setObjectName("kEdit")
        self.gridLayout.addWidget(self.kEdit, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.bEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.bEdit.setObjectName("bEdit")
        self.gridLayout.addWidget(self.bEdit, 1, 4, 1, 1)
        self.xEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.xEdit.setObjectName("xEdit")
        self.gridLayout.addWidget(self.xEdit, 3, 2, 1, 1)
        self.yEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.yEdit.setObjectName("yEdit")
        self.gridLayout.addWidget(self.yEdit, 1, 0, 1, 1)
        self.EquationTabs.addTab(self.linEq, "")
        self.sqEq = QtWidgets.QWidget()
        self.sqEq.setObjectName("sqEq")
        self.label_8 = QtWidgets.QLabel(parent=self.sqEq)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel {\n"
"    border: dashed;\n"
"    border-width: 2px;\n"
"    border-color: #CCCCCC;\n"
"    border-radius: 5px;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.sqEq)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 581, 271))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.cEdit.setObjectName("cEdit")
        self.gridLayout_2.addWidget(self.cEdit, 1, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 3, 1, 1)
        self.aEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.aEdit.setObjectName("aEdit")
        self.gridLayout_2.addWidget(self.aEdit, 1, 2, 1, 1)
        self.bEdit_2 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.bEdit_2.setObjectName("bEdit_2")
        self.gridLayout_2.addWidget(self.bEdit_2, 1, 4, 1, 1)
        self.yEdit_2 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.yEdit_2.setObjectName("yEdit_2")
        self.gridLayout_2.addWidget(self.yEdit_2, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.dEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.dEdit.setObjectName("dEdit")
        self.gridLayout_2.addWidget(self.dEdit, 3, 6, 1, 1)
        self.x1Edit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.x1Edit.setObjectName("x1Edit")
        self.gridLayout_2.addWidget(self.x1Edit, 4, 6, 1, 1)
        self.x2Edit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.x2Edit.setObjectName("x2Edit")
        self.gridLayout_2.addWidget(self.x2Edit, 5, 6, 1, 1)
        self.label_21 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 5, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 4, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 4, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 5, 4, 1, 1)
        self.ErrLabel = QtWidgets.QLabel(parent=self.sqEq)
        self.ErrLabel.setGeometry(QtCore.QRect(20, 360, 612, 16))
        self.ErrLabel.setText("")
        self.ErrLabel.setObjectName("ErrLabel")
        self.EquationTabs.addTab(self.sqEq, "")
        self.gridLayout_3.addWidget(self.EquationTabs, 0, 0, 1, 2)

        self.retranslateUi(Equation)
        self.EquationTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Equation)

    def retranslateUi(self, Equation):
        _translate = QtCore.QCoreApplication.translate
        Equation.setWindowTitle(_translate("Equation", "Уравнения"))
        self.returnBtn.setText(_translate("Equation", "Вернуться"))
        self.runBtn.setText(_translate("Equation", "Вычислить"))
        self.label.setText(_translate("Equation", "Уравнение вида y = kx + b"))
        self.label_4.setText(_translate("Equation", "x"))
        self.label_22.setText(_translate("Equation", "="))
        self.label_6.setText(_translate("Equation", "="))
        self.label_5.setText(_translate("Equation", "b"))
        self.label_7.setText(_translate("Equation", "+"))
        self.label_3.setText(_translate("Equation", "kx"))
        self.label_2.setText(_translate("Equation", "y"))
        self.yEdit.setText(_translate("Equation", "0"))
        self.EquationTabs.setTabText(self.EquationTabs.indexOf(self.linEq), _translate("Equation", "Линейное"))
        self.label_8.setText(_translate("Equation", "Уравнение вида y = ax² + bx + c"))
        self.label_12.setText(_translate("Equation", "ax²"))
        self.label_13.setText(_translate("Equation", "y"))
        self.label_15.setText(_translate("Equation", "+"))
        self.aEdit.setText(_translate("Equation", "1"))
        self.yEdit_2.setText(_translate("Equation", "0"))
        self.label_11.setText(_translate("Equation", "c"))
        self.label_10.setText(_translate("Equation", "bx"))
        self.label_14.setText(_translate("Equation", "+"))
        self.label_9.setText(_translate("Equation", "="))
        self.label_21.setText(_translate("Equation", "="))
        self.label_20.setText(_translate("Equation", "="))
        self.label_17.setText(_translate("Equation", "="))
        self.label_16.setText(_translate("Equation", "D"))
        self.label_18.setText(_translate("Equation", "x1"))
        self.label_19.setText(_translate("Equation", "x2"))
        self.EquationTabs.setTabText(self.EquationTabs.indexOf(self.sqEq), _translate("Equation", "Квадратное"))
