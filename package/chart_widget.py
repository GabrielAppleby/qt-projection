import vtkmodules.vtkRenderingOpenGL2
import vtkmodules.vtkInteractionStyle

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderer

from package.data_store import DataStore
from package.vtk_point_cloud import VtkPointCloud


class ChartWidget(QWidget):

    def __init__(self, data: DataStore, projections: DataStore) -> None:
        super(ChartWidget, self).__init__()
        self._data = data
        self._projections = projections
        self._window_layout = QVBoxLayout()
        self._vtkWidget = QVTKRenderWindowInteractor()
        self._ren = vtkRenderer()
        self._vtkWidget.GetRenderWindow().AddRenderer(self._ren)
        self._init_ui()

    def _init_ui(self) -> None:
        self._projections.data_changed.connect(self._populate_chart)
        self.setLayout(self._window_layout)

    @Slot()
    def _populate_chart(self) -> None:
        projection = self._projections.get_data()
        if projection is not None:
            point_cloud = VtkPointCloud()
            for point in projection:
                point_cloud.add_point(point)
            self._window_layout.addWidget(self._vtkWidget)
            self._ren.AddActor(point_cloud.vtkActor)
            self._ren.SetBackground(.2, .3, .4)
            self._ren.ResetCamera()
            self._ren.GetActiveCamera().Zoom(1.5)
            self._vtkWidget.Initialize()
            self._vtkWidget.Start()
