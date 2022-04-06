from PySide6.QtWidgets import QWidget, QVBoxLayout

from package.data_store import DataStore
from package.table_widget import TableWidget
from package.upload_widget import UploadWidget


class DataTab(QWidget):

    def __init__(self, data: DataStore) -> None:
        super(DataTab, self).__init__()
        self._data = data
        self._window_layout = QVBoxLayout()
        self._table_widget = TableWidget(self._data)
        self._upload_widget = UploadWidget(self._data)
        self._init_ui()

    def _init_ui(self) -> None:
        self._window_layout.addWidget(self._upload_widget)
        self._window_layout.addWidget(self._table_widget)
        self.setLayout(self._window_layout)
