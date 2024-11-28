from PyQt6.QtWidgets import QMessageBox


def show_err(self, err: Exception, *args, text="Неизвестная ошибка! Подробнее: {}"):
    QMessageBox.critical(self, "Ошибка!", text.format(err))
