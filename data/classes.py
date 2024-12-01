from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget
from math import sqrt, log

from data.functions import *

from forms.MainWindow_ui import *
from forms.EquationsWindow_ui import *
from forms.CalcWindow_ui import *


class UniversalHelper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """UniversalHelper class initialization"""
        super().__init__()
        self.setupUi(self)
        self.win = QWidget
        self.wins: list[QWidget] = []

        self.setWindowIcon(QIcon('img/favicon.ico'))

        self.eqBtn.clicked.connect(self.add_widget)
        self.calcBtn.clicked.connect(self.add_widget)

    def add_widget(self):
        self.textFrame.hide()
        try:
            match self.sender().objectName():
                case 'eqBtn':
                    self.win = EquationWindow(self)
                case 'calcBtn':
                    self.win = CalcWindow(self)
            self.wins.append(self.win)
            self.widgetsLayout.addWidget(self.win)

            self.win.returnBtn.clicked.connect(self.return_text)
        except Exception as err:
            show_err(self, err)

    def return_text(self):
        try:
            widget = self.sender().parent()
            widget.close()
            self.wins = self.wins[:self.wins.index(widget)] + self.wins[self.wins.index(widget) + 1:]
            self.resize(self.width() - widget.width(), 600)
            if not self.wins:
                self.textFrame.show()
        except Exception as err:
            show_err(self, err)


class EquationWindow(QWidget, Ui_Equation):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.runBtn.clicked.connect(self.run)

    def run(self):
        try:
            match self.EquationTabs.currentIndex():
                case 0:
                    y, k, b = (int(i) for i in (self.yEdit.text(), self.kEdit.text(), self.bEdit.text()))
                    self.xEdit.setText(str((b - y) / k))
                case 1:
                    y, a, b, c = (int(i) for i in
                                  (self.yEdit_2.text(), self.aEdit.text(), self.bEdit_2.text(), self.cEdit.text()))
                    d = (b ** 2) - 4 * (a * c)

                    self.dEdit.setText(str(d))

                    if d < 0:
                        self.ErrLabel.setText('Нет корней!')
                        self.x1Edit.setText('')
                        self.x2Edit.setText('')
                    else:
                        x1 = (- b - d ** 0.5) / (2 * a)
                        x2 = (- b + d ** 0.5) / (2 * a)
                        self.x1Edit.setText(str(x1))
                        self.x2Edit.setText(str(x2))
                        self.ErrLabel.setText('')
        except ValueError as err:
            show_err(self, err, text="Ошибка! Введено неккоректное число. Подробнее: {}")
        except Exception as err:
            show_err(self, err)


class CalcWindow(QWidget, Ui_CalcWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)

        for button in self.buttonGroup.buttons():
            button.clicked.connect(self.add_text)

        for button in self.operationsButtonGroup.buttons():
            button.clicked.connect(self.add_oper)

        self.clearBtn.clicked.connect(self.clear)
        self.backspaceBtn.clicked.connect(self.backspace)
        self.eqBtn.clicked.connect(self.run)

    def clear(self):
        self.defaultLineEdit.setText('')

    def backspace(self):
        self.defaultLineEdit.setText(self.defaultLineEdit.text()[:-1])

    def add_oper(self):
        self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} {self.sender().text()} ')

    def add_text(self):
        self.defaultLineEdit.setText(self.defaultLineEdit.text() + self.sender().text())

    def run(self):
        try:
            self.defaultLineEdit.setText(str(eval(self.defaultLineEdit.text())))
        except SyntaxError as err:
            show_err(self, err, text='Синтаксическая ошибка! Введите данные корректно')
        except Exception as err:
            show_err(self, err)