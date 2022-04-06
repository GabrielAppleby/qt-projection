from typing import Any, Union

import pandas as pd
from PySide6.QtCore import Qt, QModelIndex, QPersistentModelIndex, QAbstractTableModel


class TableModel(QAbstractTableModel):

    def __init__(self, data: pd.DataFrame) -> None:
        super(TableModel, self).__init__()
        self._data = data

    def rowCount(self,
                 parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return self._data.shape[0]

    def columnCount(self,
                    parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return self._data.shape[1]

    def data(self, index: Union[QModelIndex, QPersistentModelIndex],
             role: int = ...) -> Any:
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def flags(self, index) -> Qt.ItemFlag:
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
