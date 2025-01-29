# Импорт главного окна и всех нужных элементов

from data.classes import UniversalHelper
from PyQt6.QtWidgets import QApplication
from sys import argv, exit


def main() -> None:
    """
    Главная функция проекта

    :return: None
    """
    app = QApplication(argv)  # Создание приложения

    ex = UniversalHelper()  # Создание главного окна
    ex.show()  # Вывод главного окна на экран

    exit(app.exec())  # Закончить программу при выходе из приложения


# Если файл запущен, как главный
if __name__ == "__main__":
    main()  # Запуск главной функции
