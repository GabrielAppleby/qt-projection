import numpy as np

from vtkmodules.vtkCommonCore import vtkPoints, vtkDoubleArray
from vtkmodules.vtkCommonDataModel import vtkPolyData, vtkCellArray
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor


class VtkPointCloud:

    def __init__(self, z_min=-10.0, z_max=10.0):
        self.vtkPolyData = vtkPolyData()
        self.clear_points()
        mapper = vtkPolyDataMapper()
        mapper.SetInputData(self.vtkPolyData)
        mapper.SetColorModeToDefault()
        mapper.SetScalarRange(z_min, z_max)
        mapper.SetScalarVisibility(1)
        self.vtkActor = vtkActor()
        self.vtkActor.SetMapper(mapper)
        self.vtkActor.GetProperty().SetPointSize(10)

    def add_point(self, point: np.ndarray):
        pointId = self.vtkPoints.InsertNextPoint(point)
        self.vtkDepth.InsertNextValue(point[2])
        self.vtkCells.InsertNextCell(1)
        self.vtkCells.InsertCellPoint(pointId)
        self.vtkCells.Modified()
        self.vtkPoints.Modified()
        self.vtkDepth.Modified()

    def clear_points(self):
        self.vtkPoints = vtkPoints()
        self.vtkCells = vtkCellArray()
        self.vtkDepth = vtkDoubleArray()
        self.vtkDepth.SetName('DepthArray')
        self.vtkPolyData.SetPoints(self.vtkPoints)
        self.vtkPolyData.SetVerts(self.vtkCells)
        self.vtkPolyData.GetPointData().SetScalars(self.vtkDepth)
        self.vtkPolyData.GetPointData().SetActiveScalars('DepthArray')
