# Form implementation generated from reading ui file 'ReadMeGraphWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ReadMe(object):
    def setupUi(self, ReadMe):
        ReadMe.setObjectName("ReadMe")
        ReadMe.resize(434, 620)
        ReadMe.setStyleSheet("QWidget {\n"
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
"QLineEdit {\n"
"    font-size: 16px;\n"
"    padding: 2px; \n"
"    background-color: rgb(20, 20, 20);\n"
"    border: solid;\n"
"    border-color: #353535;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ReadMe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=ReadMe)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(parent=ReadMe)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.returnBtn = QtWidgets.QPushButton(parent=ReadMe)
        self.returnBtn.setMinimumSize(QtCore.QSize(300, 42))
        self.returnBtn.setObjectName("returnBtn")
        self.verticalLayout_2.addWidget(self.returnBtn)

        self.retranslateUi(ReadMe)
        QtCore.QMetaObject.connectSlotsByName(ReadMe)

    def retranslateUi(self, ReadMe):
        _translate = QtCore.QCoreApplication.translate
        ReadMe.setWindowTitle(_translate("ReadMe", "Справка"))
        self.label.setText(_translate("ReadMe", "Справка по использованию графиков"))
        self.textEdit.setHtml(_translate("ReadMe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">В качестве переменной используйте английский символ &quot;x&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Сложение - &quot;+&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Вычитание - &quot;-&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Умножение - &quot;*&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Деление - &quot;/&quot;    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Целочисленное деление - &quot;//&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Остаток от деления - &quot;%&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Возведение в степень - &quot;**&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Модуль - &quot;abs()&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Синус - &quot;sin()&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Косинус - &quot;cos()&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тангенс - &quot;tan()&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Котангенс - &quot;cot()&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Обратные функции - &quot;arc$func$()&quot;</p></body></html>"))
        self.returnBtn.setText(_translate("ReadMe", "Вернуться"))
