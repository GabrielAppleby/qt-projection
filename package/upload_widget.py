import pandas as pd
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog

from package.data_store import DataStore


class UploadWidget(QWidget):

    def __init__(self, data: DataStore) -> None:
        super(UploadWidget, self).__init__()
        self.button = QPushButton("Select CSV")
        self.layout = QVBoxLayout(self)
        self._data = data
        self._init_ui()

    def _init_ui(self) -> None:
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.open_file)

    @Slot()
    def open_file(self) -> None:
        filename, filter = QFileDialog.getOpenFileName(
            parent=self, caption='Open file', dir='.')
        if filename is not None and filename != '':
            file = pd.read_csv(filename)
            file = file.astype('float32')
            self._data.set_data(file)
