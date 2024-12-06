from PyQt6.QtWidgets import QMessageBox
from math import tan as t, sin as s, cos as c, radians as r, degrees as d, asin, acos, atan


def show_err(self, err: Exception, *args, text="Неизвестная ошибка! Подробнее: {}"):
    QMessageBox.critical(self, "Ошибка!", text.format(err))


def sin(x: int) -> float:
    return s(r(x))


def cos(x: int) -> float:
    return c(r(x))


def tg(x: int) -> float:
    return t(r(x))


def ctg(x: int) -> float:
    return 1 / t(x)

def arcsin(x: int) -> float:
    return asin(d(x))


def arccos(x: int) -> float:
    return acos(d(x))


def arctg(x: int) -> float:
    return atan(d(x))


def arcctg(x: int) -> float:
    pass
