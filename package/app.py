from typing import List

from PySide6.QtWidgets import QApplication

from package.main_window import MainWindow


def run(argv: List):
    app = QApplication(argv)
    ex = MainWindow()
    return app.exec()
