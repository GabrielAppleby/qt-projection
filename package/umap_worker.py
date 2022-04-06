from typing import List

import numpy as np
import pandas as pd
from PySide6.QtCore import Signal, QObject
from umap import UMAP


class UMAPWorker(QObject):
    finished = Signal(pd.DataFrame)

    def __init__(self, data: np.ndarray, hyper_params: List[int]):
        super(UMAPWorker, self).__init__()
        self._data = data
        self._hyper_params = hyper_params

    def run(self):
        projection = UMAP(n_neighbors=self._hyper_params[0], n_jobs=4).fit_transform(
            self._data)
        self.finished.emit(pd.DataFrame(projection))
