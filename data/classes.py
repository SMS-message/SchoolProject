from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from itertools import chain
from math import sqrt, log, factorial as fact
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import sqlite3

from data.functions import *

from forms.MainWindow_ui import *
from forms.EquationsWindow_ui import *
from forms.CalcWindow_ui import *
from forms.BookLibraryWindow_ui import *
from forms.GraphWindow_ui import *
from forms.ReadMeGraphWindow_ui import *
from forms.AboutWindow_ui import *


class UniversalHelper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """UniversalHelper class initialization"""
        super().__init__()
        self.setupUi(self)
        self.win: QWidget = QWidget()
        self.wins: list[QWidget] = []  # список запущенных окон

        self.setWindowIcon(QIcon('img/favicon.ico'))

        self.eqBtn.clicked.connect(self.add_widget)
        self.calcBtn.clicked.connect(self.add_widget)
        self.bookLibButton.clicked.connect(self.add_widget)
        self.graphBtn.clicked.connect(self.add_widget)

        self.authorsAction.triggered.connect(self.about)
        self.closeWinsAction.triggered.connect(self.close_widgets)
        self.exitAction.triggered.connect(self.close)

    def add_widget(self):
        self.textFrame.hide()
        try:
            match self.sender().objectName():
                case 'eqBtn':
                    self.win = EquationWindow(self)
                case 'calcBtn':
                    self.win = CalcWindow(self)
                case 'bookLibButton':
                    self.win = BookLibraryWindow(self)
                case 'graphBtn':
                    self.win = ReadMeGraphWindow(self)
                    self.wins.append(self.win)
                    self.widgetsLayout.addWidget(self.win)

                    self.win.returnBtn.clicked.connect(self.return_text)
                    self.win = GraphWindow(self)
            self.wins.append(self.win)
            self.widgetsLayout.addWidget(self.win)

            self.win.returnBtn.clicked.connect(self.return_text)
        except Exception as err:
            show_err(self, err)

    def close_widgets(self):
        while self.wins:
            self.wins.pop().close()
        self.textFrame.show()
        self.resize(672, 592)

    def about(self):
        self.win = AboutWindow(self)
        self.win.show()

    def return_text(self):
        try:
            widget = self.sender().parent()
            widget.close()
            self.wins = self.wins[:self.wins.index(widget)] + self.wins[self.wins.index(widget) + 1:]
            self.resize(self.width() - widget.width(), self.height())
            if not self.wins:
                self.textFrame.show()
        except Exception as err:
            show_err(self, err)


class EquationWindow(QWidget, Ui_Equation):
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

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.runBtn.clicked.connect(self.run)


class CalcWindow(QWidget, Ui_CalcWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)

        for button in chain(self.buttonGroup.buttons(),  # функции для кнопок с цифрами
                            self.progButtonGroup.buttons(),
                            self.engiButtonGroup.buttons()):
            button.clicked.connect(self.add_text)

        for button in chain(self.operationsButtonGroup.buttons(),  # функции для кнопок со знаками
                            self.progOperationsButtonGroup.buttons(),
                            self.engiOperationsButtonGroup.buttons()):
            button.clicked.connect(self.add_oper)

        for button in self.eqButtonGroup.buttons():  # функции для кнопок =
            button.clicked.connect(self.run)

        for button in self.clearButtonGroup.buttons():  # функции для кнопок clear
            button.clicked.connect(self.clear)

        for button in self.backspaceButtonGroup.buttons():  # функции для кнопок backspace
            button.clicked.connect(self.backspace)

        for button in self.negButtonGroup.buttons():  # функции для кнопок +/-
            button.clicked.connect(self.negative)

        for button in self.powButtonGroup.buttons():  # функции для кнопок pow
            button.clicked.connect(self.pow)

        for button in self.trigButtonGroup.buttons():  # функции для кнопок с тригонометрическими функциями
            button.clicked.connect(self.trigonometry_func)

        self.sqrtBtn.clicked.connect(self.sqrt)
        self.engiSqrtBtn.clicked.connect(self.sqrt)

        self.logBtn.clicked.connect(self.log)
        self.engiLogBtn.clicked.connect(self.log)

        self.tenPowYBtn.clicked.connect(self.pow_10)
        self.engiTenPowYBtn.clicked.connect(self.pow_10)

        self.piBtn.clicked.connect(self.pi)
        self.factBtn.clicked.connect(self.fact)

        self.progLineEdit.textChanged.connect(self.reload_numbers)
        self.progModeBox.currentIndexChanged.connect(self.reload_calc)

    def trigonometry_func(self):
        try:
            text = self.engiLineEdit.text()
            dct = {'sin': f"sin({text})", 'cos': f"cos({text})", 'tg': f"tg({text})", 'ctg': f"ctg({text})",
                   'arcsin': f"arcsin({text})", 'arccos': f"arccos({text})",
                   'arctg': f"arctg({text})", 'arcctg': f"arcctg({text})"}
            self.engiLineEdit.setText(dct[self.sender().text()])
        except Exception as err:
            show_err(self, err)

    def pi(self):
        self.engiLineEdit.setText(f"{self.engiLineEdit.text()}pi")

    def fact(self):
        self.engiLineEdit.setText(f"fact({self.engiLineEdit.text()})")

    def pow(self):
        try:
            calc = self.sender().parent().objectName()
            has_2 = ('2' if '2' in self.sender().objectName() else '')
            match calc:
                case 'Calc':
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} ** ' + has_2)
                case 'EngiCalc':
                    self.engiLineEdit.setText(f'{self.engiLineEdit.text()} ** ' + has_2)
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
                        filter(lambda x: x.strip('(').strip(')').isdigit() or {'A', 'B', 'C', 'D', 'E', 'F'} & set(x),
                               string.split()))
                    match self.progModeBox.currentText():
                        case 'HEX':
                            mapped_ints = map_ints(16, filtered_ints)
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
                            mapped_ints = mapped_ints = map_ints(8, filtered_ints)
                            res = []
                            k = 0
                            for elem in string.split():
                                if {*map(str, range(8))} & set(elem):
                                    res.append(mapped_ints[k])
                                    k += 1
                                else:
                                    res.append(elem)
                            res = ' '.join(res)
                            self.progLineEdit.setText(f'{eval(res):o}')
                        case 'BIN':
                            mapped_ints = mapped_ints = map_ints(2, filtered_ints)
                            res = []
                            k = 0
                            for elem in string.split():
                                if {'0', '1'} & set(elem):
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
            integer = int()
            match self.progModeBox.currentText():
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
        except SyntaxError as err:
            print(f'SyntaxError! {err}')
        except Exception as err:
            show_err(self, err)

    def reload_calc(self):
        match self.progModeBox.currentText():
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


class BookLibraryWindow(QWidget, Ui_studentBookLibrary):
    def __init__(self, *args, **kwargs):
        """BookLibraryWindow class initialization"""
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('db/textBookDB.db')
        self.cur = self.con.cursor()
        self.findBtn.clicked.connect(self.run)

    def run(self):
        if not self.nameLineEdit.text() and not self.authorsLineEdit.text():
            res = self.cur.execute(f"""
                                SELECT *
                                  FROM textBooks
                                 WHERE subject_id IN (
                                           SELECT ID
                                             FROM subjects
                                            WHERE subject_name = '{self.subjectBox.currentText()}'
                                       )
                                AND 
                                       grade = '{self.gradeBox.currentText()}';
                                """)

            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

class GraphWindow(QWidget, Ui_Graphs):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)

        self.runBtn.clicked.connect(self.run)

    def run(self):
        try:
            equation_str = self.graphEdit.text()
            x = sp.symbols('x')
            equation = sp.sympify(equation_str)
            f = sp.lambdify(x, equation, "numpy")

            x_vals = np.linspace(int(self.minEdit.text()), int(self.maxEdit.text()), 1000)
            y_vals = f(x_vals)

            plt.plot(x_vals, y_vals, color='black', linestyle='-', linewidth=1)
            plt.title(f'График функции: {equation_str}')
            plt.xlabel('ось x')
            plt.ylabel('ось y')
            plt.title(f'график функции y = {equation_str}')
            plt.grid(True)
            plt.show()

        except sp.SympifyError as err:
            show_err(self, err, text="Ошибка! Введено некорректное математическое выражение. Подробнее: {}")
        except Exception as err:
            show_err(self, err)


class ReadMeGraphWindow(QWidget, Ui_ReadMe):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)

class AboutWindow(QWidget, Ui_AboutUniHelp):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)