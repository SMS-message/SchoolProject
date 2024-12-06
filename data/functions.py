from PyQt6.QtWidgets import QMessageBox
from math import tan as t, sin as s, cos as c, radians as r


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
