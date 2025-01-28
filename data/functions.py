from PyQt6.QtWidgets import QMessageBox, QPushButton
from webbrowser import open_new_tab
from math import tan as t, sin as s, cos as co, radians as r, degrees as deg, asin, acos, atan, pi


def add_event_listener_to_btn(btn: QPushButton, link: str):
    btn.clicked.connect(lambda: open_new_tab(link))

def show_err(self, err: Exception, *args, text="Неизвестная ошибка! Подробнее: {}"):
    """Showing error on Exception"""
    QMessageBox.critical(self, "Ошибка!", text.format(err))


def map_ints(base: int, array: iter) -> tuple:
    """Returns tuple of ints with base 10"""
    return tuple(map(lambda x: str(int(x.strip('(').strip(')'), base)), array))


def sin(x: int | float) -> float:
    return s(r(x))


def cos(x: int | float) -> float:
    return co(r(x))


def tg(x: int | float) -> float:
    return t(r(x))


def ctg(x: int | float) -> float:
    return 1 / t(x)


def arcsin(x: int | float) -> float:
    return deg(asin(x))


def arccos(x: int) -> float:
    return deg(acos(x))


def arctg(x: int | float) -> float:
    return deg(atan(x))


def arcctg(x: int | float) -> float:
    return pi / 2 - arctg(x)
