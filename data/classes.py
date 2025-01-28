# Импорты нужных библиотек и элементов

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem, QPushButton, QButtonGroup
from itertools import chain
from math import sqrt, log, factorial as fact
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import sqlite3

# Импорт собственных функций

from data.functions import *

# Импорт интерфейсов окон
from forms.MainWindow_ui import *
from forms.EquationsWindow_ui import *
from forms.CalcWindow_ui import *
from forms.BookLibraryWindow_ui import *
from forms.GraphWindow_ui import *
from forms.ReadMeGraphWindow_ui import *
from forms.AboutWindow_ui import *


class UniversalHelper(QMainWindow, Ui_MainWindow):
    """Класс главного окна"""

    def __init__(self):
        """Инициализация класса"""
        super().__init__()
        self.setupUi(self)  #
        self.win: QWidget = QWidget()
        self.wins: list[QWidget] = []  # Список открытых окон

        self.setWindowIcon(QIcon('img/favicon.ico'))  # Установка иконки окна

        # Обработчики нажатий кнопок
        self.eqBtn.clicked.connect(self.add_widget)
        self.calcBtn.clicked.connect(self.add_widget)
        self.bookLibButton.clicked.connect(self.add_widget)
        self.graphBtn.clicked.connect(self.add_widget)

        # Обработчики нажатий на кнопки заголовка окна
        self.authorsAction.triggered.connect(self.about)
        self.closeWinsAction.triggered.connect(self.close_widgets)
        self.exitAction.triggered.connect(self.close)

    def add_widget(self) -> None:
        """
        Добавление нового виджета на экран и в список открытых окон

        :returns: None
        """
        try:  # Обработчик ошибок
            self.textFrame.hide()  # Скрывание надписи UniHelp
            match self.sender().objectName():  # Проверка совпадения названия кнопки
                case 'eqBtn':  # В случае, если нажатие произошло от кнопки "Уравнения"
                    self.win = EquationWindow(self)
                case 'calcBtn':  # В случае, если нажатие произошло от кнопки "Калькулятор"
                    self.win = CalcWindow(self)
                case 'bookLibButton':  # В случае, если нажатие произошло от кнопки "Библиотека учебников"
                    self.win = BookLibraryWindow(self)
                case 'graphBtn':  # В случае, если нажатие произошло от кнопки "Графики"
                    self.win = ReadMeGraphWindow(self)  # Добавляющееся окно - справка о графиках
                    self.wins.append(self.win)  # Добавление справки в список открытых окон
                    self.widgetsLayout.addWidget(self.win)  # Добавление справки на экран

                    self.win.returnBtn.clicked.connect(self.return_text)  # Обработчик закрытия окна справки
                    self.win = GraphWindow(self)  # Добавляющееся окно - графики
            self.wins.append(self.win)  # Добавление выбранного виджета в список открытых окон
            self.widgetsLayout.addWidget(self.win)  # Добавление выбранного виджета на экран

            self.win.returnBtn.clicked.connect(self.return_text)  # Обработчик закрытия выбранного виджета
        except Exception as err:  # В случае ошибки
            show_err(self, err)  # Уведомить пользователя об ошибке с помошью нового окна

    def close_widgets(self) -> None:
        """
        Слот для кнопки закрытия всех виджетов

        :returns: None
        """
        while self.wins:  # Пока хоть одно окно открыто
            self.wins.pop().close()  # Обращение к окну и его последующее закрытие
        self.textFrame.show()  # Показать надпись UniHelp
        self.resize(672, 592)  # Установить размер окна по умолчанию

    def about(self) -> None:
        """
        Открытие окна "О программе"

        :returns: None
        """
        self.win = AboutWindow(self)  # Открывающееся окно - "О программе"
        self.win.show()  # Показать окно на экране

    def return_text(self) -> None:
        """
        Закрытие виджета и его удаление из списка открытых окон

        :returns: None
        """
        try:
            widget = self.sender().parent()  # Выбор виджета, с которого был сигнал
            widget.close()  # Закрытие виджета на экране
            # Удаление виджета из списка открытых окон
            self.wins = self.wins[:self.wins.index(widget)] + self.wins[self.wins.index(widget) + 1:]

            self.resize(self.width() - widget.width(), self.height())  # Возвращение размера
            if not self.wins:  # Если не открыто ни одного окна
                self.textFrame.show()  # Показать надпись UniHelp
                self.resize(672, 592)  # Установить размер окна по умолчанию
        except Exception as err:
            show_err(self, err)


class EquationWindow(QWidget, Ui_Equation):
    """Окно решения уравнений"""

    def __init__(self, *args):
        """Инициализация нового окна"""
        super().__init__()
        self.setupUi(self)  # Установка интерфейса

        self.runBtn.clicked.connect(self.run)  # Обработчик нажатия на кнопку "Решить"

    def run(self) -> None:
        """
        Решение выбранного уравнения

        :returns: None
        """
        try:
            match self.EquationTabs.currentIndex():  # Выбор уравнения, которое нужно решить
                case 0:  # Решение линейного уравнения
                    y, k, b = (int(i) for i in (self.yEdit.text(), self.kEdit.text(), self.bEdit.text()))
                    self.xEdit.setText(str((b - y) / k))  # Вывод ответа на экран
                case 1:  # Решение квадратного уравнения
                    y, a, b, c = (int(i) for i in
                                  (self.yEdit_2.text(), self.aEdit.text(), self.bEdit_2.text(), self.cEdit.text()))
                    d = (b ** 2) - 4 * (a * c)  # Дискриминант

                    self.dEdit.setText(str(d))  # Вывод дискриминанта на экран

                    # Вывод результата решения на экран
                    if d < 0:
                        self.ErrLabel.setText('Нет корней!')
                        self.x1Edit.setText('')
                        self.x2Edit.setText('')
                    else:
                        x1 = (- b - d ** 0.5) / (2 * a)
                        x2 = (- b + d ** 0.5) / (2 * a)
                        self.x1Edit.setText(str(x1))  # Вывод ответа на экран
                        self.x2Edit.setText(str(x2))  # Вывод ответа на экран
                        self.ErrLabel.setText('')
        except ValueError as err:  # В случае, если введено некорректное число
            show_err(self, err, text="Ошибка! Введено некорректное число. Подробнее: {}")
        except Exception as err:  # В случае любой другой ошибка
            show_err(self, err)


class CalcWindow(QWidget, Ui_CalcWidget):
    """Окно калькулятора"""

    def __init__(self, *args, **kwargs):
        """Инициализация калькулятора"""
        super().__init__()
        self.setupUi(self)

        # Обработчики нажатий для кнопок с цифрами
        for button in chain(self.buttonGroup.buttons(),
                            self.progButtonGroup.buttons(),
                            self.engiButtonGroup.buttons()):
            button.clicked.connect(self.add_text)

        # Обработчики нажатий для кнопок со знаками
        for button in chain(self.operationsButtonGroup.buttons(),
                            self.progOperationsButtonGroup.buttons(),
                            self.engiOperationsButtonGroup.buttons()):
            button.clicked.connect(self.add_oper)

        # Обработчики нажатий для кнопок "="
        for button in self.eqButtonGroup.buttons():
            button.clicked.connect(self.run)

        # Обработчики нажатий для кнопок clear
        for button in self.clearButtonGroup.buttons():
            button.clicked.connect(self.clear)

        # Обработчики нажатий для кнопок backspace
        for button in self.backspaceButtonGroup.buttons():
            button.clicked.connect(self.backspace)

        # Обработчики нажатий для кнопок "+/-"
        for button in self.negButtonGroup.buttons():
            button.clicked.connect(self.negative)

        # Обработчики нажатий для кнопок pow
        for button in self.powButtonGroup.buttons():
            button.clicked.connect(self.pow)

        # Обработчики нажатий для кнопок с тригонометрическими функциями
        for button in self.trigButtonGroup.buttons():
            button.clicked.connect(self.trigonometry_func)

        # Обработчики нажатий для кнопок sqrt
        self.sqrtBtn.clicked.connect(self.sqrt)
        self.engiSqrtBtn.clicked.connect(self.sqrt)

        # Обработчики нажатий для кнопок log
        self.logBtn.clicked.connect(self.log)
        self.engiLogBtn.clicked.connect(self.log)

        # Обработчики нажатий для кнопок 10^y
        self.tenPowYBtn.clicked.connect(self.pow_10)
        self.engiTenPowYBtn.clicked.connect(self.pow_10)

        # Обработчики нажатий для кнопок п
        self.piBtn.clicked.connect(self.pi)
        self.factBtn.clicked.connect(self.fact)

        # Обработчики изменений для калькулятора систем счисления
        self.progLineEdit.textChanged.connect(self.reload_numbers)
        self.progModeBox.currentIndexChanged.connect(self.reload_calc)

    def trigonometry_func(self) -> None:
        """
        Установка текста в тригонометрическую функцию

        :returns: None
        """
        try:
            text = self.engiLineEdit.text()  # Текст, который находится на экране
            # Словарь для установления соответствий
            dct = {'sin': f"sin({text})", 'cos': f"cos({text})", 'tg': f"tg({text})", 'ctg': f"ctg({text})",
                   'arcsin': f"arcsin({text})", 'arccos': f"arccos({text})",
                   'arctg': f"arctg({text})", 'arcctg': f"arcctg({text})"}

            self.engiLineEdit.setText(dct[self.sender().text()])  # Обновление текста на экране
        except Exception as err:
            show_err(self, err)

    def pi(self) -> None:
        """
        Добавление числа п на экран

        :returns: None
        """
        self.engiLineEdit.setText(f"{self.engiLineEdit.text()}pi")

    def fact(self) -> None:
        """
        Добавление факториала на экран

        :returns: None
        """
        self.engiLineEdit.setText(f"fact({self.engiLineEdit.text()})")

    def pow(self) -> None:
        """
        Добавление возведения в степень на экран

        :returns: None
        """
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            has_2 = ('2' if '2' in self.sender().objectName() else '')  # Если сигнал с кнопки возведения в квадрат
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} ** ' + has_2)
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(f'{self.engiLineEdit.text()} ** ' + has_2)
        except Exception as err:
            show_err(self, err)

    def pow_10(self) -> None:
        """
        Добавление умножения на десять в степени y на экран

        :returns: None
        """
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(
                        f'{self.defaultLineEdit.text()} * 10 ** ' if self.defaultLineEdit.text() else '(10 ** ')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(
                        f'{self.engiLineEdit.text()} * 10 ** ' if self.engiLineEdit.text() else '(10 ** ')
        except Exception as err:
            show_err(self, err)

    def sqrt(self) -> None:
        """
        Добавление корня на экран

        :returns: None
        """
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(f'sqrt({self.defaultLineEdit.text()})')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(f'sqrt({self.engiLineEdit.text()})')
        except Exception as err:
            show_err(self, err)

    def log(self) -> None:
        """
        Добавление логарифма на экран

        :returns: None
        """
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(f'log({self.defaultLineEdit.text()}, ')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(f'log({self.engiLineEdit.text()}, ')
        except Exception as err:
            show_err(self, err)

    def abs(self) -> None:
        """
        Добавление модуля на экран

        :returns: None
        """
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(f'abs({self.defaultLineEdit.text()}) ')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(f'abs({self.engiLineEdit.text()}) ')
        except Exception as err:
            show_err(self, err)

    def clear(self) -> None:
        """
        Очистка поля ввода

        :returns: None
        """
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText('')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText('')
                case 'ProgCalc':  # Если сигнал пришёл с калькулятора систем счисления
                    self.progLineEdit.setText('')
        except Exception as err:
            show_err(self, err)

    def backspace(self) -> None:
        """
        Удаление последнего символа в поле ввода

        :returns: None
        """
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(self.defaultLineEdit.text()[:-1])
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(f'{self.engiLineEdit.text()[:-1]}')
                case 'ProgCalc':  # Если сигнал пришёл с калькулятора систем счисления
                    self.progLineEdit.setText(f'{self.progLineEdit.text()[:-1]}')
        except Exception as err:
            show_err(self, err)

    def negative(self) -> None:  # TODO: Комментарии ко всем функциям
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(f'-{self.defaultLineEdit.text()}')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(f'-{self.engiLineEdit.text()}')
                case 'ProgCalc':  # Если сигнал пришёл с калькулятора систем счисления
                    self.progLineEdit.setText(f'-{self.progLineEdit.text()}')
        except Exception as err:
            show_err(self, err)

    def add_oper(self) -> None:
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(f'{self.defaultLineEdit.text()} {self.sender().text()} ')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(f'{self.engiLineEdit.text()} {self.sender().text()} ')
                case 'ProgCalc':  # Если сигнал пришёл с калькулятора систем счисления
                    self.progLineEdit.setText(f'{self.progLineEdit.text()} {self.sender().text()} ')
        except Exception as err:
            show_err(self, err)

    def add_text(self) -> None:
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    if self.defaultLineEdit.text() and self.defaultLineEdit.text()[
                        -1].isdigit() and not ',' in self.defaultLineEdit.text():
                        self.defaultLineEdit.setText(
                            f'{self.defaultLineEdit.text()}{self.sender().text()}'.replace(',', '.', 1))
                    else:
                        self.defaultLineEdit.setText(
                            f'{self.defaultLineEdit.text()}{self.sender().text()}')
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    if self.engiLineEdit.text() and self.engiLineEdit.text()[
                        -1].isdigit() and not ',' in self.engiLineEdit.text():
                        self.engiLineEdit.setText(
                            f'{self.engiLineEdit.text()}{self.sender().text()}'.replace(',', '.', 1))
                    else:
                        self.engiLineEdit.setText(
                            f'{self.engiLineEdit.text()}{self.sender().text()}')
                case 'ProgCalc':  # Если сигнал пришёл с калькулятора систем счисления
                    self.progLineEdit.setText(f'{self.progLineEdit.text()}{self.sender().text()}')

        except Exception as err:
            show_err(self, err)

    def run(self) -> None:
        try:
            calc = self.sender().parent().objectName()  # Выбор калькулятора, с которого пришёл сигнал
            match calc:
                case 'Calc':  # Если сигнал пришёл с обычного калькулятора
                    self.defaultLineEdit.setText(str(eval(self.defaultLineEdit.text())))
                case 'EngiCalc':  # Если сигнал пришёл с инженерного калькулятора
                    self.engiLineEdit.setText(str(eval(self.engiLineEdit.text())))
                case 'ProgCalc':  # Если сигнал пришёл с калькулятора систем счисления
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
                            mapped_ints = map_ints(8, filtered_ints)
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

    def reload_numbers(self) -> None:
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

    def reload_calc(self) -> None:
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
        try:
            self.tableWidget.clear()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            request = "SELECT name, link FROM textBooks "
            texts = {"grade": ('' if self.gradeBox.currentText() == "Любой" else self.gradeBox.currentText()),
                     "subject_id": ('' if self.subjectBox.currentText() == "Любой" else self.subjectBox.currentIndex()),
                     "author_id": self.authorsLineEdit.text(), "name": self.nameLineEdit.text()}
            if any(texts.values()):
                request += "WHERE "
                flag = False
                for key, value in texts.items():
                    if not value:
                        continue
                    if flag:
                        request += " AND "
                    match key:
                        case "author_id":
                            request += f"{key} IN (SELECT ID FROM authors WHERE author_surname LIKE '%{value}%')"
                            flag = True
                            continue
                        case "name":
                            request += f"{key} LIKE '%{value}%'"
                            flag = True
                            continue
                    request += f"{key}={value}"
                    flag = True
            print(request)
            res = self.cur.execute(request)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(("Учебник", "Ссылка"))
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    if j == 1:
                        button = QPushButton()
                        button.setText("Скачать")
                        add_event_listener_to_btn(button, str(elem))
                        self.tableWidget.setCellWidget(i, j, button)
                    else:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
            self.tableWidget.setColumnWidth(0, 200)
            self.tableWidget.setColumnWidth(1, 100)
        except Exception as err:
            show_err(self, err)


class GraphWindow(QWidget, Ui_Graphs):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)

        self.runBtn.clicked.connect(self.run)

    def run(self):
        try:
            x = sp.symbols('x')
            equation = sp.sympify(self.graphEdit.text())
            f = sp.lambdify(x, equation, "numpy")

            x_vals = np.linspace(int(self.minEdit.text()), int(self.maxEdit.text()), 1000)
            y_vals = f(x_vals)

            plt.plot(x_vals, y_vals, color='black', linestyle='-', linewidth=1)
            plt.title(f'График функции: {self.graphEdit.text()}')
            plt.xlabel('ось x')
            plt.ylabel('ось y')
            plt.title(f'график функции y = {self.graphEdit.text()}')
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
