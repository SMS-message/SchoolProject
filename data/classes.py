from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt
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

        self.xPow2Btn.clicked.connect(self.pow_2)
        self.xPowYBtn.clicked.connect(self.pow_y)
        self.tenPowYBtn.clicked.connect(self.pow_10)
        self.sqrtBtn.clicked.connect(self.sqrt)
        self.logBtn.clicked.connect(self.log)
        self.absBtn.clicked.connect(self.abs)
        self.negBtn.clicked.connect(self.negative)

        for button in self.progButtonGroup.buttons():
            button.clicked.connect(self.add_text_prog)

        for button in self.progOperationsButtonGroup.buttons():
            button.clicked.connect(self.add_oper_prog)

        self.progEqBtn.clicked.connect(self.run_prog)
        self.progClearBtn.clicked.connect(self.clear_prog)
        self.progBackspaceBtn.clicked.connect(self.backspace_prog)
        self.progNegBtn.clicked.connect(self.negative_prog)

        self.progLineEdit.textChanged.connect(self.reload_numbers)
        self.comboBox.currentIndexChanged.connect(self.reload_calc)

    def keyPressEvent(self, event):
        try:
            match event.key():
                case Qt.Key.Key_Return:
                    self.run()
                case Qt.Key.Key_1:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}1')
                case Qt.Key.Key_2:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}2')
                case Qt.Key.Key_3:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}3')
                case Qt.Key.Key_4:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}4')
                case Qt.Key.Key_5:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}5')
                case Qt.Key.Key_6:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}6')
                case Qt.Key.Key_7:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}7')
                case Qt.Key.Key_8:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}8')
                case Qt.Key.Key_9:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}9')
                case Qt.Key.Key_0:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()}0')
                case Qt.Key.Key_Plus:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} + ')
                case Qt.Key.Key_Minus:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} - ')
                case Qt.Key.Key_division:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} / ')
                case Qt.Key.Key_multiply:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} * ')
                case Qt.Key.Key_AsciiCircum:
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} ** ')
                case Qt.Key.Key_Backspace:
                    self.backspace()

        except Exception as err:
            show_err(self, err)

    def negative(self):
        self.defaultLineEdit.setText(f'-{self.defaultLineEdit.text()}')

    def negative_prog(self):
        self.progLineEdit.setText(f'-{self.progLineEdit.text()}')

    def pow_2(self):
        self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} ** 2 ')

    def pow_y(self):
        self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} ** ')

    def pow_10(self):
        self.defaultLineEdit.setText(
            f'{self.defaultLineEdit.text()} * 10 ** ' if self.defaultLineEdit.text() else '(10 ** ')

    def sqrt(self):
        self.defaultLineEdit.setText(f'sqrt({self.defaultLineEdit.text()}) ')

    def log(self):
        self.defaultLineEdit.setText(f'log({self.defaultLineEdit.text()}, ')

    def abs(self):
        self.defaultLineEdit.setText(f'abs({self.defaultLineEdit.text()}) ')

    def clear(self):
        self.defaultLineEdit.setText('')

    def clear_prog(self):
        self.progLineEdit.setText('')

    def backspace(self):
        self.defaultLineEdit.setText(self.defaultLineEdit.text()[:-1])

    def backspace_prog(self):
        self.progLineEdit.setText(f'{self.progLineEdit.text()[:-1]}')

    def add_oper(self):
        self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} {self.sender().text()} ')

    def add_oper_prog(self):
        self.progLineEdit.setText(f'{self.progLineEdit.text()} {self.sender().text()} ')

    def add_text(self):
        try:
            if self.defaultLineEdit.text() and self.defaultLineEdit.text()[
                -1].isdigit() and not ',' in self.defaultLineEdit.text():
                self.defaultLineEdit.setText(
                    f'{self.defaultLineEdit.text()}{self.sender().text()}'.replace(',', '.', 1))
            else:
                self.defaultLineEdit.setText(
                    f'{self.defaultLineEdit.text()}{self.sender().text()}')
        except Exception as err:
            show_err(self, err)

    def add_text_prog(self):
        try:
            self.progLineEdit.setText(f'{self.progLineEdit.text()}{self.sender().text()}')
        except Exception as err:
            show_err(self, err)

    def run(self):
        try:
            self.defaultLineEdit.setText(str(eval(self.defaultLineEdit.text())))
        except SyntaxError as err:
            show_err(self, err, text='Синтаксическая ошибка! Введите данные корректно')
        except Exception as err:
            show_err(self, err)

    def run_prog(self):
        try:
            string = self.progLineEdit.text()
            filtered_ints = tuple(
                filter(lambda x: x.strip('(').isdigit() or {'A', 'B', 'C', 'D', 'E', 'F'} & set(x), string.split()))
            match self.comboBox.currentText():
                case 'HEX':
                    mapped_ints = tuple(map(lambda x: str(int(x, 16)), filtered_ints))
                    res = []
                    k = 0
                    for elem in string.split():
                        if elem.isdigit() or {'A', 'B', 'C', 'D', 'E', 'F'} & set(elem):
                            res.append(mapped_ints[k])
                            k += 1
                        else:
                            res.append(elem)
                    res = ' '.join(res)
                    self.progLineEdit.setText(f'{eval(res):x}'.upper())
                case 'DEC':
                    res = self.progLineEdit.text()
                    self.progLineEdit.setText(f'{eval(res)}')
                case 'OCT':
                    mapped_ints = tuple(map(lambda x: int(x, 8), filtered_ints))
                    res = []
                    k = 0
                    for elem in string.split():
                        if elem.isdigit() or {'A', 'B', 'C', 'D', 'E', 'F'} & set(elem):
                            res.append(mapped_ints[k])
                            k += 1
                        else:
                            res.append(elem)
                    res = ' '.join(res)
                    self.progLineEdit.setText(f'{eval(res):o}')
                case 'BIN':
                    mapped_ints = tuple(map(lambda x: int(x, 10), filtered_ints))
                    res = []
                    k = 0
                    for elem in string.split():
                        if elem.isdigit() or {'A', 'B', 'C', 'D', 'E', 'F'} & set(elem):
                            res.append(mapped_ints[k])
                            k += 1
                        else:
                            res.append(elem)
                    res = ' '.join(res)
                    self.progLineEdit.setText(f'{eval(res):b}')
            self.reload_numbers()
        except SyntaxError as err:
            show_err(self, err, text='Синтаксическая ошибка! Введите данные корректно')
        except Exception as err:
            show_err(self, err)

    def reload_numbers(self):
        try:
            if {'+', '-', '*', '<', '>', '%', '/', '(', ')'} & set(self.progLineEdit.text()):
                return
            if not self.progLineEdit.text():
                self.hexEdit.setText('0')
                self.decEdit.setText('0')
                self.octEdit.setText('0')
                self.binEdit.setText('0')
                return
            match self.comboBox.currentText():
                case 'HEX':
                    integer = int(self.progLineEdit.text(), 16)
                case 'DEC':
                    integer = int(self.progLineEdit.text())
                case 'OCT':
                    integer = int(self.progLineEdit.text(), 8)
                case 'BIN':
                    integer = int(self.progLineEdit.text(), 2)
            self.hexEdit.setText(f'{integer:x}'.upper())
            self.decEdit.setText(f'{integer:}')
            self.octEdit.setText(f'{integer:o}')
            self.binEdit.setText(f'{integer:b}')
        except Exception as err:
            show_err(self, err)

    def reload_calc(self):
        match self.comboBox.currentText():
            case 'HEX':
                self.progTwoBtn.setDisabled(False)
                self.progThreeBtn.setDisabled(False)
                self.progFourBtn.setDisabled(False)
                self.progFiveBtn.setDisabled(False)
                self.progSixBtn.setDisabled(False)
                self.progSevenBtn.setDisabled(False)
                self.progEightBtn.setDisabled(False)
                self.progNineBtn.setDisabled(False)
                self.progABtn.setDisabled(False)
                self.progBBtn.setDisabled(False)
                self.progCBtn.setDisabled(False)
                self.progDBtn.setDisabled(False)
                self.progEBtn.setDisabled(False)
                self.progFBtn.setDisabled(False)
            case 'DEC':
                self.progTwoBtn.setDisabled(False)
                self.progThreeBtn.setDisabled(False)
                self.progFourBtn.setDisabled(False)
                self.progFiveBtn.setDisabled(False)
                self.progSixBtn.setDisabled(False)
                self.progSevenBtn.setDisabled(False)
                self.progEightBtn.setDisabled(False)
                self.progNineBtn.setDisabled(False)
                self.progABtn.setDisabled(True)
                self.progBBtn.setDisabled(True)
                self.progCBtn.setDisabled(True)
                self.progDBtn.setDisabled(True)
                self.progEBtn.setDisabled(True)
                self.progFBtn.setDisabled(True)
            case 'OCT':
                self.progTwoBtn.setDisabled(False)
                self.progThreeBtn.setDisabled(False)
                self.progFourBtn.setDisabled(False)
                self.progFiveBtn.setDisabled(False)
                self.progSixBtn.setDisabled(False)
                self.progSevenBtn.setDisabled(False)
                self.progEightBtn.setDisabled(True)
                self.progNineBtn.setDisabled(True)
                self.progABtn.setDisabled(True)
                self.progBBtn.setDisabled(True)
                self.progCBtn.setDisabled(True)
                self.progDBtn.setDisabled(True)
                self.progEBtn.setDisabled(True)
                self.progFBtn.setDisabled(True)
            case 'BIN':
                self.progTwoBtn.setDisabled(True)
                self.progThreeBtn.setDisabled(True)
                self.progFourBtn.setDisabled(True)
                self.progFiveBtn.setDisabled(True)
                self.progSixBtn.setDisabled(True)
                self.progSevenBtn.setDisabled(True)
                self.progEightBtn.setDisabled(True)
                self.progNineBtn.setDisabled(True)
                self.progABtn.setDisabled(True)
                self.progBBtn.setDisabled(True)
                self.progCBtn.setDisabled(True)
                self.progDBtn.setDisabled(True)
                self.progEBtn.setDisabled(True)
                self.progFBtn.setDisabled(True)