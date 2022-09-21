from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from package.data_store import DataStore
from package.data_tab import DataTab
from package.projection_tab import ProjectionTab


class MainWindow(QWidget):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.title = 'Projector'
        self._data = DataStore()
        self._tab_widget = QTabWidget()
        self._window_layout = QVBoxLayout()
        self._data_tab = DataTab(self._data)
        self._projection_tab = ProjectionTab(self._data)

        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle(self.title)
        self.showMaximized()
        self._window_layout.addWidget(self._tab_widget)
        self._tab_widget.addTab(self._data_tab, 'Data')
        self._tab_widget.addTab(self._projection_tab, 'Projection')
        self.setLayout(self._window_layout)
