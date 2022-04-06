import pandas as pd
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog
from sklearn.datasets import fetch_openml

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

    def open_file(self) -> None:
        images, _ = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=True)
        print(images.values.dtype)
        print(images.shape)
        self._data.set_data(images)
        # filename, filter = QFileDialog.getOpenFileName(
        #     parent=self, caption='Open file', dir='.')
        # if filename is not None and filename != '':
        #     file = pd.read_csv(filename)
        #     self._data.set_data(file)
