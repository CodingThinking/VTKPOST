#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:10:40 2016

@author: wang
"""
import vtk
# VTK处理集
class VTK_NodeSet(object):
    
    def __init__(self,nodes,key = 'float'):
        self.Node = [ tuple(x) for x in nodes]
        self.NodeNumber = len(self.Node)
        self.Title = 'POINTS' + ' ' +\
                     str(self.NodeNumber) + ' ' + key

class VTK_2PLineSet(object):
    
    def __init__(self,member):
        self.Line = [ tuple(x) for x in member]
        self.LineNumber = len(self.Line)
        self.DataNumber = 3*self.LineNumber
        self.Title = 'LINES' + ' ' +\
                      str(self.LineNumber) + ' ' +\
                      str(self.DataNumber)
        
class VTK_ScalarData(object):
    
    def __init__(self,DataSet,name,DataType = 'float',SepNumber = 1,TableNumber = 1):
        self.Title = 'SCALARS' + name +\
                     ' ' + DataType +\
                     ' ' + str(SepNumber)
        if isinstance(DataSet,dict):
            self.err = 'DataSet is not dict'
            self.DataSet = []
            self.Name = []
        else:
            for x in DataSet:
                title = 'LOOKUP_TABLE' + ' ' + x
                if len(DataSet[x][0]) is not 1:
                    title = title + ' ' + str(len(DataSet[x]))
                self.DataSet[title] = DataSet[x]
                self.Name[x] = title
    
    def AddTable(self,DataDict):
        for x in DataDict:
            title = 'LOOKUP_TABLE' + ' ' + x
            if len(DataDict[x][0]) is not 1:
                title = title + ' ' + str(len(DataDict[x]))
            self.DataSet[title] = DataDict[x]
            self.Name[x] = title
            
    def DelTable(self,NameList):
        for x in NameList:
            if x in self.Name:
                self.DataSet.pop(self.Name[x])
            
        

class VTK_VecterData(object):
    
    def __init__(self,name,DataSet,DataType = 'float'):
        self.Title = 'VECTORS' + ' ' +\
                      name + ' ' + DataType
        self.DataSet = DataSet
        
        
class VTK_Model(object):
    
    def __init__(self,name,version = 2.0,CodeType = 'ASCII',DATASET = 'POLYDATA'):
        self.vtk_version = version
        self.name = name
        self.CodeType = CodeType
        self.DataSet = DATASET
        self.Points = []
        self.element = []
        self.CellData = []
        self.PointData = []
    
    def GetPoints(self,p):
        if isinstance(p,VTK_NodeSet):
            self.Points = p
        else:
            self.Points = VTK_NodeSet(p)
        
    def GetElement(self,ele):
        if isinstance(ele,VTK_2PLineSet):
            self.element = ele
        else:
            self.element = VTK_2PLineSet(ele)
    
    def GetCellData(self,data):
        self.CellData.append(data)
    
    def GetPointData(self,data):
        self.CellData.append(data)
        
    def ModelIni(self):
        
        Grid = vtk.vtkPolyData()
        Points = vtk.vtkPoints()
        for x in self.Points.Node:
            Points.InsertNextPoint(x[0],x[1],x[2])

        lines = vtk.vtkCellArray()
        line = vtk.vtkLine()
        for x in self.element.Line:
            line.GetPointIds().SetId(0, x[0])
            line.GetPointIds().SetId(1, x[1])
            lines.InsertNextCell(line)
            
        Grid.SetPoints(Points)
        Grid.SetLines(lines)
        if vtk.VTK_MAJOR_VERSION <= 5:
            Grid.Update()
        source = Grid
        
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(source)
        
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetRepresentationToWireframe()
        actor.GetProperty().SetColor(255,255,255)
        
        renderer = vtk.vtkRenderer()
        renWin = vtk.vtkRenderWindow()
        renWin.AddRenderer(renderer)
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(renWin)
        
        renderer.AddActor(actor)
        renderer.SetBackground(84/255,89/255,109/255)
        renderer.ResetCamera()        
        renderer.GetActiveCamera().ParallelProjectionOn()
        
        renWin.SetSize(600, 600)
        
        self.model = {'RenderWindow':renWin,
                      'iterRender':iren}
        
    def GraphShow(self):
        self.model['RenderWindow'].Render()
        self.model['iterRender'].Start()
        


        
class VTK_FileReader(object):

    def __init__(self,FilePath,Name):
        self.Name = Name
        self.File = FilePath
        
    def IniModel(self):
        reader = vtk.vtkPolyDataReader()
        reader.SetFileName(self.FilePath)
        reader.Update()
    
        
