from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget
from itertools import chain
from math import sqrt, log, pi, factorial as fact

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

        for button in chain(self.buttonGroup.buttons(),  # функции для кнопок с цифрами
                            self.progButtonGroup.buttons(),
                            self.engiButtonGroup.buttons()):
            button.clicked.connect(self.add_text)

        for button in chain(self.operationsButtonGroup.buttons(), # функции для кнопок со знаками
                            self.progOperationsButtonGroup.buttons(),
                            self.engiOperationsButtonGroup.buttons()):
            button.clicked.connect(self.add_oper)

        for button in self.eqButtonGroup.buttons(): # функции для кнопок =
            button.clicked.connect(self.run)

        for button in self.clearButtonGroup.buttons():  # функции для кнопок clear
            button.clicked.connect(self.clear)

        for button in self.backspaceButtonGroup.buttons():  # функции для кнопок backspace
            button.clicked.connect(self.backspace)

        for button in self.negButtonGroup.buttons():  # функции для кнопок +/-
            button.clicked.connect(self.negative)

        for button in self.powButtonGroup.buttons():  # функции для кнопок pow
            button.clicked.connect(self.pow)

        self.sqrtBtn.clicked.connect(self.sqrt)
        self.engiSqrtBtn.clicked.connect(self.sqrt)

        self.progLineEdit.textChanged.connect(self.reload_numbers)
        self.comboBox.currentIndexChanged.connect(self.reload_calc)

        self.piBtn.clicked.connect(self.pi)
        self.factBtn.clicked.connect(self.fact)

        self.sinBtn.clicked.connect(self.sin)
        self.cosBtn.clicked.connect(self.cos)
        self.tgBtn.clicked.connect(self.tg)
        self.ctgBtn.clicked.connect(self.ctg)
        self.arcSinBtn.clicked.connect(self.arcsin)
        self.arcCosBtn.clicked.connect(self.arccos)
        self.arcTgBtn.clicked.connect(self.arctg)
        self.arcCtgBtn.clicked.connect(self.arcctg)

    def pi(self):
        self.engiLineEdit.setText(f"{self.engiLineEdit.text()}pi")

    def sin(self):
        self.engiLineEdit.setText(f"sin({self.engiLineEdit.text()})")

    def cos(self):
        self.engiLineEdit.setText(f"cos({self.engiLineEdit.text()})")

    def tg(self):
        self.engiLineEdit.setText(f"tg({self.engiLineEdit.text()})")

    def ctg(self):
        self.engiLineEdit.setText(f"ctg({self.engiLineEdit.text()})")

    def arcsin(self):
        self.engiLineEdit.setText(f"arcsin({self.engiLineEdit.text()})")

    def arccos(self):
        self.engiLineEdit.setText(f"arccos({self.engiLineEdit.text()})")

    def arctg(self):
        self.engiLineEdit.setText(f"arctg({self.engiLineEdit.text()})")

    def arcctg(self):
        self.engiLineEdit.setText(f"arcctg({self.engiLineEdit.text()})")

    def fact(self):
        self.engiLineEdit.setText(f"fact({self.engiLineEdit.text()})")

    def pow(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} ** ' +
                                                 '2' if '2' in self.sender().objectName() else '')
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'{self.engiLineEdit.text()} ** ' +
                                              '2' if '2' in self.sender().objectName() else '')
        except Exception as err:
            show_err(self, err)

    def pow_10(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(
                        f'{self.defaultLineEdit.text()} * 10 ** ' if self.defaultLineEdit.text() else '(10 ** ')
                case 'EngiCalc':
                    self.engiLineEdit.setText(
                        f'{self.engiLineEdit.text()} * 10 ** ' if self.engiLineEdit.text() else '(10 ** ')
        except Exception as err:
            show_err(self, err)

    def sqrt(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(f'sqrt({self.defaultLineEdit.text()})')
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'sqrt({self.engiLineEdit.text()})')
        except Exception as err:
            show_err(self, err)

    def log(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(f'log({self.defaultLineEdit.text()}, ')
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'log({self.engiLineEdit.text()}, ')
        except Exception as err:
            show_err(self, err)

    def abs(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(f'abs({self.defaultLineEdit.text()}) ')
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'abs({self.engiLineEdit.text()}) ')
        except Exception as err:
            show_err(self, err)

    def clear(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText('')
                case 'EngiCalc':
                    self.engiLineEdit.setText('')
                case 'ProgCalc':
                    self.progLineEdit.setText('')
        except Exception as err:
            show_err(self, err)

    def backspace(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(self.defaultLineEdit.text()[:-1])
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'{self.engiLineEdit.text()[:-1]}')
                case 'ProgCalc':
                    self.progLineEdit.setText(f'{self.progLineEdit.text()[:-1]}')
        except Exception as err:
            show_err(self, err)

    def negative(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(f'-{self.defaultLineEdit.text()}')
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'-{self.engiLineEdit.text()}')
                case 'ProgCalc':
                    self.progLineEdit.setText(f'-{self.progLineEdit.text()}')
        except Exception as err:
            show_err(self, err)

    def add_oper(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} {self.sender().text()} ')
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'{self.engiLineEdit.text()} {self.sender().text()} ')
                case 'ProgCalc':
                    self.progLineEdit.setText(f'{self.progLineEdit.text()} {self.sender().text()} ')
        except Exception as err:
            show_err(self, err)

    def add_text(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    if self.defaultLineEdit.text() and self.defaultLineEdit.text()[
                        -1].isdigit() and not ',' in self.defaultLineEdit.text():
                        self.defaultLineEdit.setText(
                            f'{self.defaultLineEdit.text()}{self.sender().text()}'.replace(',', '.', 1))
                    else:
                        self.defaultLineEdit.setText(
                            f'{self.defaultLineEdit.text()}{self.sender().text()}')
                case 'EngiCalc':
                    if self.engiLineEdit.text() and self.engiLineEdit.text()[
                        -1].isdigit() and not ',' in self.engiLineEdit.text():
                        self.engiLineEdit.setText(
                            f'{self.engiLineEdit.text()}{self.sender().text()}'.replace(',', '.', 1))
                    else:
                        self.engiLineEdit.setText(
                            f'{self.engiLineEdit.text()}{self.sender().text()}')
                case 'ProgCalc':
                    self.progLineEdit.setText(f'{self.progLineEdit.text()}{self.sender().text()}')

        except Exception as err:
            show_err(self, err)

    def run(self):
        try:
            calc = self.sender().parent().objectName()
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(str(eval(self.defaultLineEdit.text())))
                case 'EngiCalc':
                    self.engiLineEdit.setText(str(eval(self.engiLineEdit.text())))
                case 'ProgCalc':
                    string = self.progLineEdit.text()
                    filtered_ints = tuple(
                        filter(lambda x: x.strip('(').isdigit() or {'A', 'B', 'C', 'D', 'E', 'F'} & set(x),
                               string.split()))
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
