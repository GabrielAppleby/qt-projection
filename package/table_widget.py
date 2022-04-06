from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QAbstractButton

from package.data_store import DataStore
from package.table_model import TableModel


class TableWidget(QWidget):

    def __init__(self, data: DataStore) -> None:
        super(TableWidget, self).__init__()
        self._data = data
        self._table_view = QTableView()
        self._window_layout = QVBoxLayout()
        self._init_ui()

    def _init_ui(self) -> None:
        self._data.data_changed.connect(self._set_table_model)
        self._window_layout.addWidget(self._table_view)
        self.setLayout(self._window_layout)

    def _set_table_model(self) -> None:
        data = self._data.get_data()
        if data is not None:
            self.table_model = TableModel(data)
            self.proxy_model = QSortFilterProxyModel()
            self.proxy_model.setSourceModel(self.table_model)
            self._table_view.setSortingEnabled(True)
            self._table_view.setModel(self.proxy_model)
            corner_button = self._table_view.findChild(QAbstractButton)
            corner_button.clicked.connect(lambda: self.proxy_model.sort(-1))
