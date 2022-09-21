from PySide6.QtCore import QThread, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from package.data_store import DataStore
from package.umap_worker import UMAPWorker


class ProjectionWidget(QWidget):

    def __init__(self, data: DataStore, projections: DataStore) -> None:
        super(ProjectionWidget, self).__init__()
        self._data = data
        self._projections = projections
        self._projectionWorker = None
        self._projectionThread = QThread()
        self._button = QPushButton("Project")
        self._window_layout = QVBoxLayout()
        self._init_ui()

    def _init_ui(self) -> None:
        self._button.clicked.connect(self._project)
        self._window_layout.addWidget(self._button)
        self.setLayout(self._window_layout)

    @Slot()
    def _project(self) -> None:
        self._projectionWorker = UMAPWorker(self._data.get_data().values, [5])
        self._projectionWorker.moveToThread(self._projectionThread)
        self._projectionThread.started.connect(self._projectionWorker.run)
        self._projectionWorker.finished.connect(self._projections.set_data)
        self._projectionWorker.finished.connect(self._projectionThread.quit)
        self._projectionThread.start()
