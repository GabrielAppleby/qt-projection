from PySide6.QtCharts import QChartView, QChart, QScatterSeries
from PySide6.QtCore import QPointF
from PySide6.QtGui import QColorConstants
from PySide6.QtWidgets import QWidget, QVBoxLayout

from package.data_store import DataStore


class ChartWidget(QWidget):

    def __init__(self, data: DataStore, projections: DataStore) -> None:
        super(ChartWidget, self).__init__()
        self._data = data
        self._projections = projections
        self._series = QScatterSeries()
        self._chart = QChart()
        self._chart_view = QChartView()
        self._window_layout = QVBoxLayout()
        self._init_ui()

    def _init_ui(self) -> None:
        self._projections.data_changed.connect(self._populate_chart)
        self._chart_view.setChart(self._chart)
        self._window_layout.addWidget(self._chart_view)
        self.setLayout(self._window_layout)

    def _populate_chart(self) -> None:
        projection = self._projections.get_data()
        if projection is not None:
            extrema = projection.agg([min, max])
            projection = projection.values
            data_points = [QPointF(i[0], i[1]) for i in projection]
            self._series.replace(data_points)
            self._series.setMarkerSize(8)
            # self._series.setBorderColor(QColorConstants.Transparent)
            marker_size = 2
            self._chart.addSeries(self._series)
            self._chart.createDefaultAxes()
            self._chart.axisX().setRange(extrema.loc['min', 0] - marker_size, extrema.loc['max', 0] + marker_size)
            self._chart.axisY().setRange(extrema.loc['min', 1] - marker_size, extrema.loc['max', 1] + marker_size)
            self._chart.legend().hide()
