# Form implementation generated from reading ui file 'BookLibraryWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_studentBookLibrary(object):
    def setupUi(self, studentBookLibrary):
        studentBookLibrary.setObjectName("studentBookLibrary")
        studentBookLibrary.resize(800, 600)
        studentBookLibrary.setMinimumSize(QtCore.QSize(800, 0))
        studentBookLibrary.setMaximumSize(QtCore.QSize(800, 16777215))
        studentBookLibrary.setStyleSheet("QWidget {\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(studentBookLibrary)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=studentBookLibrary)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=studentBookLibrary)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gradeBox = QtWidgets.QComboBox(parent=studentBookLibrary)
        self.gradeBox.setMinimumSize(QtCore.QSize(70, 0))
        self.gradeBox.setObjectName("gradeBox")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.gradeBox.addItem("")
        self.horizontalLayout.addWidget(self.gradeBox)
        self.label_2 = QtWidgets.QLabel(parent=studentBookLibrary)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.subjectBox = QtWidgets.QComboBox(parent=studentBookLibrary)
        self.subjectBox.setMinimumSize(QtCore.QSize(130, 0))
        self.subjectBox.setObjectName("subjectBox")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.subjectBox.addItem("")
        self.horizontalLayout.addWidget(self.subjectBox)
        self.label_3 = QtWidgets.QLabel(parent=studentBookLibrary)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.authorsLineEdit = QtWidgets.QLineEdit(parent=studentBookLibrary)
        self.authorsLineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.authorsLineEdit.setObjectName("authorsLineEdit")
        self.horizontalLayout.addWidget(self.authorsLineEdit)
        self.label_4 = QtWidgets.QLabel(parent=studentBookLibrary)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.nameLineEdit = QtWidgets.QLineEdit(parent=studentBookLibrary)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout.addWidget(self.nameLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.findBtn = QtWidgets.QPushButton(parent=studentBookLibrary)
        self.findBtn.setMinimumSize(QtCore.QSize(150, 30))
        self.findBtn.setObjectName("findBtn")
        self.horizontalLayout_3.addWidget(self.findBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.returnBtn = QtWidgets.QPushButton(parent=studentBookLibrary)
        self.returnBtn.setMinimumSize(QtCore.QSize(150, 30))
        self.returnBtn.setObjectName("returnBtn")
        self.horizontalLayout_4.addWidget(self.returnBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(studentBookLibrary)
        QtCore.QMetaObject.connectSlotsByName(studentBookLibrary)

    def retranslateUi(self, studentBookLibrary):
        _translate = QtCore.QCoreApplication.translate
        studentBookLibrary.setWindowTitle(_translate("studentBookLibrary", "Библиотека учебников"))
        self.label.setText(_translate("studentBookLibrary", "Класс:"))
        self.gradeBox.setItemText(0, _translate("studentBookLibrary", "Любой"))
        self.gradeBox.setItemText(1, _translate("studentBookLibrary", "1"))
        self.gradeBox.setItemText(2, _translate("studentBookLibrary", "2"))
        self.gradeBox.setItemText(3, _translate("studentBookLibrary", "3"))
        self.gradeBox.setItemText(4, _translate("studentBookLibrary", "4"))
        self.gradeBox.setItemText(5, _translate("studentBookLibrary", "5"))
        self.gradeBox.setItemText(6, _translate("studentBookLibrary", "6"))
        self.gradeBox.setItemText(7, _translate("studentBookLibrary", "7"))
        self.gradeBox.setItemText(8, _translate("studentBookLibrary", "8"))
        self.gradeBox.setItemText(9, _translate("studentBookLibrary", "9"))
        self.gradeBox.setItemText(10, _translate("studentBookLibrary", "10"))
        self.gradeBox.setItemText(11, _translate("studentBookLibrary", "11"))
        self.label_2.setText(_translate("studentBookLibrary", "Предмет:"))
        self.subjectBox.setItemText(0, _translate("studentBookLibrary", "Любой"))
        self.subjectBox.setItemText(1, _translate("studentBookLibrary", "Математика"))
        self.subjectBox.setItemText(2, _translate("studentBookLibrary", "Геометрия"))
        self.subjectBox.setItemText(3, _translate("studentBookLibrary", "Алгебра"))
        self.subjectBox.setItemText(4, _translate("studentBookLibrary", "Физика"))
        self.subjectBox.setItemText(5, _translate("studentBookLibrary", "Информатика"))
        self.subjectBox.setItemText(6, _translate("studentBookLibrary", "Химия"))
        self.subjectBox.setItemText(7, _translate("studentBookLibrary", "Биология"))
        self.subjectBox.setItemText(8, _translate("studentBookLibrary", "Английский язык"))
        self.subjectBox.setItemText(9, _translate("studentBookLibrary", "Русский язык"))
        self.subjectBox.setItemText(10, _translate("studentBookLibrary", "Литература"))
        self.subjectBox.setItemText(11, _translate("studentBookLibrary", "История"))
        self.subjectBox.setItemText(12, _translate("studentBookLibrary", "Обществознание"))
        self.subjectBox.setItemText(13, _translate("studentBookLibrary", "География"))
        self.label_3.setText(_translate("studentBookLibrary", "Авторы:"))
        self.label_4.setText(_translate("studentBookLibrary", "Название:"))
        self.findBtn.setText(_translate("studentBookLibrary", "Найти"))
        self.returnBtn.setText(_translate("studentBookLibrary", "Вернуться"))
