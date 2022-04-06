from PySide6.QtWidgets import QWidget, QVBoxLayout

from package.chart_widget import ChartWidget
from package.data_store import DataStore
from package.projection_widget import ProjectionWidget


class ProjectionTab(QWidget):

    def __init__(self, data: DataStore) -> None:
        super(ProjectionTab, self).__init__()
        self._data = data
        self._projections = DataStore()
        self._projector = ProjectionWidget(self._data, self._projections)
        self._chart = ChartWidget(self._data, self._projections)
        self._window_layout = QVBoxLayout()
        self._init_ui()

    def _init_ui(self) -> None:
        self._window_layout.addWidget(self._projector)
        self._window_layout.addWidget(self._chart)
        self.setLayout(self._window_layout)
