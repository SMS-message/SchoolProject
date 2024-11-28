from data.classes import UniversalHelper
from PyQt6.QtWidgets import QApplication
import sys


def main(*args, **kwargs) -> None:
    """main function"""
    app = QApplication(sys.argv)  # TODO: Покакать; by: gerod; date: 28.11.2024

    ex = UniversalHelper()
    ex.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
