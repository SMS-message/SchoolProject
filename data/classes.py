from PyQt6 import QtWidgets, QtCore
from data.functions import *

from forms.MainWindow_ui import *
from forms.EquationsWindow_ui import *


class UniversalHelper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """UniversalHelper class initialization"""
        super().__init__()
        self.setupUi(self)
        self.win = QtWidgets.QWidget()

        self.eqBtn.clicked.connect(self.open_eq_win)

    def open_eq_win(self):
        try:
            self.win = EquationWindow(self)

            self.horizontalLayout.addWidget(self.win)
            self.resize(int(self.width() * 1.2), 600)
            self.textFrame.hide()

            self.win.returnBtn.clicked.connect(self.return_text)

        except Exception as err:
            show_err(self, err)

    def return_text(self):
        try:
            self.win.hide()
            self.textFrame.show()
            self.resize(800, 600)

        except Exception as err:
            show_err(self, err)


class EquationWindow(QtWidgets.QWidget, Ui_Equation):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.runBtn.clicked.connect(self.run)
        # self.returnBtn.clicked.connect(self.rtrn)

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
