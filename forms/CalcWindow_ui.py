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
        CalcWidget.resize(330, 574)
        CalcWidget.setMaximumSize(QtCore.QSize(330, 16777215))
        CalcWidget.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: rgb(18, 18, 18);\n"
"    font-family: Open Sans;\n"
"}\n"
"\n"
"Line {\n"
"    border: 1px;\n"
"    background:  #CCCCCC;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"\n"
"    width: 50px;\n"
"    height: 40px;\n"
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
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #353535;\n"
"}\n"
"")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(CalcWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(parent=CalcWidget)
        self.tabWidget.setStyleSheet("QLineEdit {\n"
"    font-size: 16px;\n"
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
        self.tabWidget.setObjectName("tabWidget")
        self.Calc = QtWidgets.QWidget()
        self.Calc.setObjectName("Calc")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Calc)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.defaultLineEdit = QtWidgets.QLineEdit(parent=self.Calc)
        self.defaultLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.defaultLineEdit.setText("")
        self.defaultLineEdit.setObjectName("defaultLineEdit")
        self.verticalLayout.addWidget(self.defaultLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.engiCalcLayout = QtWidgets.QGridLayout()
        self.engiCalcLayout.setVerticalSpacing(2)
        self.engiCalcLayout.setObjectName("engiCalcLayout")
        self.openBracketBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.openBracketBtn.setObjectName("openBracketBtn")
        self.buttonGroup = QtWidgets.QButtonGroup(CalcWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.openBracketBtn)
        self.engiCalcLayout.addWidget(self.openBracketBtn, 1, 1, 1, 1)
        self.logBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.logBtn.setObjectName("logBtn")
        self.engiCalcLayout.addWidget(self.logBtn, 5, 0, 1, 1)
        self.threeBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.threeBtn.setObjectName("threeBtn")
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
        self.buttonGroup.addButton(self.comBtn)
        self.engiCalcLayout.addWidget(self.comBtn, 5, 3, 1, 1)
        self.closeBracketBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.closeBracketBtn.setObjectName("closeBracketBtn")
        self.buttonGroup.addButton(self.closeBracketBtn)
        self.engiCalcLayout.addWidget(self.closeBracketBtn, 1, 2, 1, 1)
        self.tenPowYBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.tenPowYBtn.setObjectName("tenPowYBtn")
        self.engiCalcLayout.addWidget(self.tenPowYBtn, 4, 0, 1, 1)
        self.subBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.subBtn.setObjectName("subBtn")
        self.operationsButtonGroup = QtWidgets.QButtonGroup(CalcWidget)
        self.operationsButtonGroup.setObjectName("operationsButtonGroup")
        self.operationsButtonGroup.addButton(self.subBtn)
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
        self.operationsButtonGroup.addButton(self.divBtn)
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
        self.operationsButtonGroup.addButton(self.mulBtn)
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
        self.operationsButtonGroup.addButton(self.addBtn)
        self.engiCalcLayout.addWidget(self.addBtn, 4, 4, 1, 1)
        self.xPow2Btn = QtWidgets.QPushButton(parent=self.Calc)
        self.xPow2Btn.setObjectName("xPow2Btn")
        self.engiCalcLayout.addWidget(self.xPow2Btn, 1, 0, 1, 1)
        self.clearBtn = QtWidgets.QPushButton(parent=self.Calc)
        self.clearBtn.setStyleSheet("QPushButton:hover {\n"
"    border-color: #AA7744;\n"
"    border-width: 2px;\n"
"\n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-color: #FFCC11;\n"
"    border-width: 2px;\n"
"    \n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.clearBtn.setObjectName("clearBtn")
        self.engiCalcLayout.addWidget(self.clearBtn, 0, 3, 1, 1)
        self.backspaceBtn = QtWidgets.QPushButton(parent=self.Calc)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.backspaceBtn.setFont(font)
        self.backspaceBtn.setStyleSheet("QPushButton:hover {\n"
"    border-color: #774444;\n"
"    border-width: 2px;\n"
"\n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-color: #CC0000;\n"
"    border-width: 2px;\n"
"    \n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.backspaceBtn.setObjectName("backspaceBtn")
        self.engiCalcLayout.addWidget(self.backspaceBtn, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.engiCalcLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.Calc, "")
        self.ProgCalc = QtWidgets.QWidget()
        self.ProgCalc.setStyleSheet("QComboBox {\n"
"    border-color: #353535;\n"
"}")
        self.ProgCalc.setObjectName("ProgCalc")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ProgCalc)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.progLineEdit = QtWidgets.QLineEdit(parent=self.ProgCalc)
        self.progLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.progLineEdit.setText("")
        self.progLineEdit.setObjectName("progLineEdit")
        self.verticalLayout_7.addWidget(self.progLineEdit)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.ProgCalc)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.hexEdit = QtWidgets.QLineEdit(parent=self.ProgCalc)
        self.hexEdit.setStyleSheet("QLineEdit {\n"
"    font-size: 12px;\n"
"}")
        self.hexEdit.setReadOnly(True)
        self.hexEdit.setObjectName("hexEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.hexEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.ProgCalc)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.decEdit = QtWidgets.QLineEdit(parent=self.ProgCalc)
        self.decEdit.setStyleSheet("QLineEdit {\n"
"    font-size: 12px;\n"
"}")
        self.decEdit.setReadOnly(True)
        self.decEdit.setObjectName("decEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.decEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.ProgCalc)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.octEdit = QtWidgets.QLineEdit(parent=self.ProgCalc)
        self.octEdit.setStyleSheet("QLineEdit {\n"
"    font-size: 12px;\n"
"}")
        self.octEdit.setReadOnly(True)
        self.octEdit.setObjectName("octEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.octEdit)
        self.label_6 = QtWidgets.QLabel(parent=self.ProgCalc)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.line = QtWidgets.QFrame(parent=self.ProgCalc)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.line)
        self.label_3 = QtWidgets.QLabel(parent=self.ProgCalc)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(parent=self.ProgCalc)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.binEdit = QtWidgets.QLineEdit(parent=self.ProgCalc)
        self.binEdit.setStyleSheet("QLineEdit {\n"
"    font-size: 12px;\n"
"}")
        self.binEdit.setReadOnly(True)
        self.binEdit.setObjectName("binEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.binEdit)
        self.verticalLayout_7.addLayout(self.formLayout)
        self.progCalcLayout = QtWidgets.QGridLayout()
        self.progCalcLayout.setVerticalSpacing(2)
        self.progCalcLayout.setObjectName("progCalcLayout")
        self.progBBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progBBtn.setObjectName("progBBtn")
        self.progButtonGroup = QtWidgets.QButtonGroup(CalcWidget)
        self.progButtonGroup.setObjectName("progButtonGroup")
        self.progButtonGroup.addButton(self.progBBtn)
        self.progCalcLayout.addWidget(self.progBBtn, 1, 0, 1, 1)
        self.progOneBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progOneBtn.setObjectName("progOneBtn")
        self.progButtonGroup.addButton(self.progOneBtn)
        self.progCalcLayout.addWidget(self.progOneBtn, 4, 1, 1, 1)
        self.openBracketBtn_5 = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.openBracketBtn_5.setObjectName("openBracketBtn_5")
        self.progButtonGroup.addButton(self.openBracketBtn_5)
        self.progCalcLayout.addWidget(self.openBracketBtn_5, 1, 1, 1, 1)
        self.progSubBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progSubBtn.setObjectName("progSubBtn")
        self.progOperationsButtonGroup = QtWidgets.QButtonGroup(CalcWidget)
        self.progOperationsButtonGroup.setObjectName("progOperationsButtonGroup")
        self.progOperationsButtonGroup.addButton(self.progSubBtn)
        self.progCalcLayout.addWidget(self.progSubBtn, 3, 4, 1, 1)
        self.progFourBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progFourBtn.setObjectName("progFourBtn")
        self.progButtonGroup.addButton(self.progFourBtn)
        self.progCalcLayout.addWidget(self.progFourBtn, 3, 1, 1, 1)
        self.progComBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progComBtn.setText("")
        self.progComBtn.setObjectName("progComBtn")
        self.progButtonGroup.addButton(self.progComBtn)
        self.progCalcLayout.addWidget(self.progComBtn, 5, 3, 1, 1)
        self.progBackspaceBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.progBackspaceBtn.setFont(font)
        self.progBackspaceBtn.setStyleSheet("QPushButton:hover {\n"
"    border-color: #774444;\n"
"    border-width: 2px;\n"
"\n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-color: #CC0000;\n"
"    border-width: 2px;\n"
"    \n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.progBackspaceBtn.setObjectName("progBackspaceBtn")
        self.progCalcLayout.addWidget(self.progBackspaceBtn, 0, 4, 1, 1)
        self.progEqBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progEqBtn.setObjectName("progEqBtn")
        self.progCalcLayout.addWidget(self.progEqBtn, 5, 4, 1, 1)
        self.progSixBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progSixBtn.setObjectName("progSixBtn")
        self.progButtonGroup.addButton(self.progSixBtn)
        self.progCalcLayout.addWidget(self.progSixBtn, 3, 3, 1, 1)
        self.progEightBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progEightBtn.setObjectName("progEightBtn")
        self.progButtonGroup.addButton(self.progEightBtn)
        self.progCalcLayout.addWidget(self.progEightBtn, 2, 2, 1, 1)
        self.progAddBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progAddBtn.setObjectName("progAddBtn")
        self.progOperationsButtonGroup.addButton(self.progAddBtn)
        self.progCalcLayout.addWidget(self.progAddBtn, 4, 4, 1, 1)
        self.progEBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progEBtn.setObjectName("progEBtn")
        self.progButtonGroup.addButton(self.progEBtn)
        self.progCalcLayout.addWidget(self.progEBtn, 4, 0, 1, 1)
        self.progSevenBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progSevenBtn.setObjectName("progSevenBtn")
        self.progButtonGroup.addButton(self.progSevenBtn)
        self.progCalcLayout.addWidget(self.progSevenBtn, 2, 1, 1, 1)
        self.progABtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progABtn.setObjectName("progABtn")
        self.progButtonGroup.addButton(self.progABtn)
        self.progCalcLayout.addWidget(self.progABtn, 0, 0, 1, 1)
        self.progThreeBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progThreeBtn.setObjectName("progThreeBtn")
        self.progButtonGroup.addButton(self.progThreeBtn)
        self.progCalcLayout.addWidget(self.progThreeBtn, 4, 3, 1, 1)
        self.progMulBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progMulBtn.setObjectName("progMulBtn")
        self.progOperationsButtonGroup.addButton(self.progMulBtn)
        self.progCalcLayout.addWidget(self.progMulBtn, 2, 4, 1, 1)
        self.progNegBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progNegBtn.setObjectName("progNegBtn")
        self.progCalcLayout.addWidget(self.progNegBtn, 5, 1, 1, 1)
        self.absBtn_5 = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.absBtn_5.setObjectName("absBtn_5")
        self.progOperationsButtonGroup.addButton(self.absBtn_5)
        self.progCalcLayout.addWidget(self.absBtn_5, 1, 3, 1, 1)
        self.progFBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progFBtn.setObjectName("progFBtn")
        self.progButtonGroup.addButton(self.progFBtn)
        self.progCalcLayout.addWidget(self.progFBtn, 5, 0, 1, 1)
        self.zeroBtn_5 = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.zeroBtn_5.setObjectName("zeroBtn_5")
        self.progButtonGroup.addButton(self.zeroBtn_5)
        self.progCalcLayout.addWidget(self.zeroBtn_5, 5, 2, 1, 1)
        self.progTwoBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progTwoBtn.setObjectName("progTwoBtn")
        self.progButtonGroup.addButton(self.progTwoBtn)
        self.progCalcLayout.addWidget(self.progTwoBtn, 4, 2, 1, 1)
        self.closeBracketBtn_5 = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.closeBracketBtn_5.setObjectName("closeBracketBtn_5")
        self.progButtonGroup.addButton(self.closeBracketBtn_5)
        self.progCalcLayout.addWidget(self.closeBracketBtn_5, 1, 2, 1, 1)
        self.progClearBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progClearBtn.setStyleSheet("QPushButton:hover {\n"
"    border-color: #AA7744;\n"
"    border-width: 2px;\n"
"\n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-color: #FFCC11;\n"
"    border-width: 2px;\n"
"    \n"
"    width: 300px;\n"
"    height: 30px;\n"
"}\n"
"")
        self.progClearBtn.setObjectName("progClearBtn")
        self.progCalcLayout.addWidget(self.progClearBtn, 0, 3, 1, 1)
        self.progCBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progCBtn.setObjectName("progCBtn")
        self.progButtonGroup.addButton(self.progCBtn)
        self.progCalcLayout.addWidget(self.progCBtn, 2, 0, 1, 1)
        self.progDBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progDBtn.setObjectName("progDBtn")
        self.progButtonGroup.addButton(self.progDBtn)
        self.progCalcLayout.addWidget(self.progDBtn, 3, 0, 1, 1)
        self.progNineBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progNineBtn.setObjectName("progNineBtn")
        self.progButtonGroup.addButton(self.progNineBtn)
        self.progCalcLayout.addWidget(self.progNineBtn, 2, 3, 1, 1)
        self.leftBitShiftBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.leftBitShiftBtn.setObjectName("leftBitShiftBtn")
        self.progOperationsButtonGroup.addButton(self.leftBitShiftBtn)
        self.progCalcLayout.addWidget(self.leftBitShiftBtn, 0, 1, 1, 1)
        self.progFiveBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progFiveBtn.setObjectName("progFiveBtn")
        self.progButtonGroup.addButton(self.progFiveBtn)
        self.progCalcLayout.addWidget(self.progFiveBtn, 3, 2, 1, 1)
        self.progDivBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.progDivBtn.setObjectName("progDivBtn")
        self.progOperationsButtonGroup.addButton(self.progDivBtn)
        self.progCalcLayout.addWidget(self.progDivBtn, 1, 4, 1, 1)
        self.rightBitShiftBtn = QtWidgets.QPushButton(parent=self.ProgCalc)
        self.rightBitShiftBtn.setObjectName("rightBitShiftBtn")
        self.progOperationsButtonGroup.addButton(self.rightBitShiftBtn)
        self.progCalcLayout.addWidget(self.rightBitShiftBtn, 0, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.progCalcLayout)
        self.tabWidget.addTab(self.ProgCalc, "")
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
        self.tabWidget.setCurrentIndex(1)
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
        self.clearBtn.setText(_translate("CalcWidget", "CE"))
        self.backspaceBtn.setText(_translate("CalcWidget", "⌫"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Calc), _translate("CalcWidget", "Обычный"))
        self.label.setText(_translate("CalcWidget", "HEX"))
        self.hexEdit.setText(_translate("CalcWidget", "0"))
        self.label_2.setText(_translate("CalcWidget", "DEC"))
        self.decEdit.setText(_translate("CalcWidget", "0"))
        self.label_5.setText(_translate("CalcWidget", "OCT"))
        self.octEdit.setText(_translate("CalcWidget", "0"))
        self.label_6.setText(_translate("CalcWidget", "BIN"))
        self.label_3.setText(_translate("CalcWidget", "Mode:"))
        self.comboBox.setItemText(0, _translate("CalcWidget", "HEX"))
        self.comboBox.setItemText(1, _translate("CalcWidget", "DEC"))
        self.comboBox.setItemText(2, _translate("CalcWidget", "OCT"))
        self.comboBox.setItemText(3, _translate("CalcWidget", "BIN"))
        self.binEdit.setText(_translate("CalcWidget", "0"))
        self.progBBtn.setText(_translate("CalcWidget", "B"))
        self.progOneBtn.setText(_translate("CalcWidget", "1"))
        self.openBracketBtn_5.setText(_translate("CalcWidget", "("))
        self.progSubBtn.setText(_translate("CalcWidget", "-"))
        self.progFourBtn.setText(_translate("CalcWidget", "4"))
        self.progBackspaceBtn.setText(_translate("CalcWidget", "⌫"))
        self.progEqBtn.setText(_translate("CalcWidget", "="))
        self.progSixBtn.setText(_translate("CalcWidget", "6"))
        self.progEightBtn.setText(_translate("CalcWidget", "8"))
        self.progAddBtn.setText(_translate("CalcWidget", "+"))
        self.progEBtn.setText(_translate("CalcWidget", "E"))
        self.progSevenBtn.setText(_translate("CalcWidget", "7"))
        self.progABtn.setText(_translate("CalcWidget", "A"))
        self.progThreeBtn.setText(_translate("CalcWidget", "3"))
        self.progMulBtn.setText(_translate("CalcWidget", "*"))
        self.progNegBtn.setText(_translate("CalcWidget", "+/-"))
        self.absBtn_5.setText(_translate("CalcWidget", "%"))
        self.progFBtn.setText(_translate("CalcWidget", "F"))
        self.zeroBtn_5.setText(_translate("CalcWidget", "0"))
        self.progTwoBtn.setText(_translate("CalcWidget", "2"))
        self.closeBracketBtn_5.setText(_translate("CalcWidget", ")"))
        self.progClearBtn.setText(_translate("CalcWidget", "CE"))
        self.progCBtn.setText(_translate("CalcWidget", "C"))
        self.progDBtn.setText(_translate("CalcWidget", "D"))
        self.progNineBtn.setText(_translate("CalcWidget", "9"))
        self.leftBitShiftBtn.setText(_translate("CalcWidget", "<<"))
        self.progFiveBtn.setText(_translate("CalcWidget", "5"))
        self.progDivBtn.setText(_translate("CalcWidget", "/"))
        self.rightBitShiftBtn.setText(_translate("CalcWidget", ">>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProgCalc), _translate("CalcWidget", "Системы счисления"))
        self.returnBtn.setText(_translate("CalcWidget", "Вернуться"))
