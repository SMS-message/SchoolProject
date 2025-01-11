from data.classes import UniversalHelper
from PyQt6.QtWidgets import QApplication
import sys


def main() -> None:
    """main function"""
    app = QApplication(sys.argv)

    ex = UniversalHelper()
    ex.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
#арбузыыыыыыыыыыыыыыыыыыыы