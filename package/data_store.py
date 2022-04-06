from typing import Union

import pandas as pd
from PySide6.QtCore import Signal, QObject


class DataStore(QObject):
    data_changed = Signal()

    def __init__(self, data: Union[pd.DataFrame, None] = None):
        super(DataStore, self).__init__()
        self._data = data

    def get_data(self) -> Union[pd.DataFrame, None]:
        return self._data

    def set_data(self, data: Union[pd.DataFrame, None]):
        self._data = data
        self.data_changed.emit()
