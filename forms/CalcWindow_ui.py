# Form implementation generated from reading ui file 'CalcWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CalcWidget(object):
    def setupUi(self, CalcWidget):
        CalcWidget.setObjectName("CalcWidget")
        CalcWidget.resize(330, 409)
        CalcWidget.setMaximumSize(QtCore.QSize(330, 16777215))
        CalcWidget.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: rgb(18, 18, 18);\n"
"    font-family: Open Sans;\n"
"}\n"
"\n"
"QPushButton {\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: #FFF;\n"
"    background-color: #303030;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color: #353535;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #454545;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-color: #FFF;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: #FFF;\n"
"    background-color: #303030;\n"
"    \n"
"    border: solid;\n"
"    border-color: #353535;\n"
"    border-width: 1px;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(CalcWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(parent=CalcWidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: none;\n"
"    border-top: 1px solid #353535;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #303030;\n"
"    \n"
"    height: 20px;\n"
"    border: solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.Calc = QtWidgets.QWidget()
        self.Calc.setObjectName("Calc")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Calc)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.defaultLineEdit = QtWidgets.QLineEdit(parent=self.Calc)
        self.defaultLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.defaultLineEdit.setObjectName("defaultLineEdit")
        self.verticalLayout.addWidget(self.defaultLineEdit)
        self.engiCalcLayout = QtWidgets.QGridLayout()
        self.engiCalcLayout.setVerticalSpacing(2)
        self.engiCalcLayout.setObjectName("engiCalcLayout")
        self.openBracketBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.openBracketBtn.setObjectName("openBracketBtn")
        self.engiCalcLayout.addWidget(self.openBracketBtn, 1, 1, 1, 1)
        self.logBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.logBtn.setObjectName("logBtn")
        self.engiCalcLayout.addWidget(self.logBtn, 5, 0, 1, 1)
        self.threeBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.threeBtn.setObjectName("threeBtn")
        self.buttonGroup = QtWidgets.QButtonGroup(CalcWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.threeBtn)
        self.engiCalcLayout.addWidget(self.threeBtn, 4, 3, 1, 1)
        self.fiveBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.fiveBtn.setObjectName("fiveBtn")
        self.buttonGroup.addButton(self.fiveBtn)
        self.engiCalcLayout.addWidget(self.fiveBtn, 3, 2, 1, 1)
        self.eightBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.eightBtn.setObjectName("eightBtn")
        self.buttonGroup.addButton(self.eightBtn)
        self.engiCalcLayout.addWidget(self.eightBtn, 2, 2, 1, 1)
        self.twoBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.twoBtn.setObjectName("twoBtn")
        self.buttonGroup.addButton(self.twoBtn)
        self.engiCalcLayout.addWidget(self.twoBtn, 4, 2, 1, 1)
        self.absBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.absBtn.setObjectName("absBtn")
        self.engiCalcLayout.addWidget(self.absBtn, 1, 3, 1, 1)
        self.negBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.negBtn.setObjectName("negBtn")
        self.engiCalcLayout.addWidget(self.negBtn, 5, 1, 1, 1)
        self.comBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.comBtn.setObjectName("comBtn")
        self.engiCalcLayout.addWidget(self.comBtn, 5, 3, 1, 1)
        self.closeBracketBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.closeBracketBtn.setObjectName("closeBracketBtn")
        self.engiCalcLayout.addWidget(self.closeBracketBtn, 1, 2, 1, 1)
        self.tenPowYBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.tenPowYBtn.setObjectName("tenPowYBtn")
        self.engiCalcLayout.addWidget(self.tenPowYBtn, 4, 0, 1, 1)
        self.subBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.subBtn.setObjectName("subBtn")
        self.engiCalcLayout.addWidget(self.subBtn, 3, 4, 1, 1)
        self.oneBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.oneBtn.setObjectName("oneBtn")
        self.buttonGroup.addButton(self.oneBtn)
        self.engiCalcLayout.addWidget(self.oneBtn, 4, 1, 1, 1)
        self.xPowYBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.xPowYBtn.setObjectName("xPowYBtn")
        self.engiCalcLayout.addWidget(self.xPowYBtn, 2, 0, 1, 1)
        self.divBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.divBtn.setObjectName("divBtn")
        self.engiCalcLayout.addWidget(self.divBtn, 1, 4, 1, 1)
        self.nineBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.nineBtn.setObjectName("nineBtn")
        self.buttonGroup.addButton(self.nineBtn)
        self.engiCalcLayout.addWidget(self.nineBtn, 2, 3, 1, 1)
        self.zeroBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.zeroBtn.setObjectName("zeroBtn")
        self.buttonGroup.addButton(self.zeroBtn)
        self.engiCalcLayout.addWidget(self.zeroBtn, 5, 2, 1, 1)
        self.mulBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.mulBtn.setObjectName("mulBtn")
        self.engiCalcLayout.addWidget(self.mulBtn, 2, 4, 1, 1)
        self.eqBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.eqBtn.setObjectName("eqBtn")
        self.engiCalcLayout.addWidget(self.eqBtn, 5, 4, 1, 1)
        self.sevenBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.sevenBtn.setObjectName("sevenBtn")
        self.buttonGroup.addButton(self.sevenBtn)
        self.engiCalcLayout.addWidget(self.sevenBtn, 2, 1, 1, 1)
        self.fourBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.fourBtn.setObjectName("fourBtn")
        self.buttonGroup.addButton(self.fourBtn)
        self.engiCalcLayout.addWidget(self.fourBtn, 3, 1, 1, 1)
        self.sqrtBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.sqrtBtn.setObjectName("sqrtBtn")
        self.engiCalcLayout.addWidget(self.sqrtBtn, 3, 0, 1, 1)
        self.sixBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.sixBtn.setObjectName("sixBtn")
        self.buttonGroup.addButton(self.sixBtn)
        self.engiCalcLayout.addWidget(self.sixBtn, 3, 3, 1, 1)
        self.addBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.addBtn.setObjectName("addBtn")
        self.engiCalcLayout.addWidget(self.addBtn, 4, 4, 1, 1)
        self.xPow2Btn = QtWidgets.QPushButton(parent=self.Calc)
        self.xPow2Btn.setObjectName("xPow2Btn")
        self.engiCalcLayout.addWidget(self.xPow2Btn, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.engiCalcLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.tabWidget.addTab(self.Calc, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.errLabel = QtWidgets.QLabel(parent=CalcWidget)
        self.errLabel.setText("")
        self.errLabel.setObjectName("errLabel")
        self.verticalLayout_5.addWidget(self.errLabel)
        self.returnBtn = QtWidgets.QPushButton(parent=CalcWidget)
        self.returnBtn.setMaximumSize(QtCore.QSize(320, 16777215))
        self.returnBtn.setObjectName("returnBtn")
        self.verticalLayout_5.addWidget(self.returnBtn)

        self.retranslateUi(CalcWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CalcWidget)

    def retranslateUi(self, CalcWidget):
        _translate = QtCore.QCoreApplication.translate
        CalcWidget.setWindowTitle(_translate("CalcWidget", "Калькулятор"))
        self.openBracketBtn.setText(_translate("CalcWidget", "("))
        self.logBtn.setText(_translate("CalcWidget", "log"))
        self.threeBtn.setText(_translate("CalcWidget", "3"))
        self.fiveBtn.setText(_translate("CalcWidget", "5"))
        self.eightBtn.setText(_translate("CalcWidget", "8"))
        self.twoBtn.setText(_translate("CalcWidget", "2"))
        self.absBtn.setText(_translate("CalcWidget", "|x|"))
        self.negBtn.setText(_translate("CalcWidget", "+/-"))
        self.comBtn.setText(_translate("CalcWidget", ","))
        self.closeBracketBtn.setText(_translate("CalcWidget", ")"))
        self.tenPowYBtn.setText(_translate("CalcWidget", "10ʸ"))
        self.subBtn.setText(_translate("CalcWidget", "-"))
        self.oneBtn.setText(_translate("CalcWidget", "1"))
        self.xPowYBtn.setText(_translate("CalcWidget", "xʸ"))
        self.divBtn.setText(_translate("CalcWidget", "/"))
        self.nineBtn.setText(_translate("CalcWidget", "9"))
        self.zeroBtn.setText(_translate("CalcWidget", "0"))
        self.mulBtn.setText(_translate("CalcWidget", "*"))
        self.eqBtn.setText(_translate("CalcWidget", "="))
        self.sevenBtn.setText(_translate("CalcWidget", "7"))
        self.fourBtn.setText(_translate("CalcWidget", "4"))
        self.sqrtBtn.setText(_translate("CalcWidget", "√"))
        self.sixBtn.setText(_translate("CalcWidget", "6"))
        self.addBtn.setText(_translate("CalcWidget", "+"))
        self.xPow2Btn.setText(_translate("CalcWidget", "x²"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Calc), _translate("CalcWidget", "Обычный"))
        self.returnBtn.setText(_translate("CalcWidget", "Вернуться"))
