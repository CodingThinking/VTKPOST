#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1
@author: Wang
@mail: 11212035w@zju.edu.cn
@software: PyCharm
@file: 1.py
@time: 2016/3/21 21:59
"""
__author__ = 'wang'

import PyQt4.QtGui as PyQtGui
import PyQt4.QtCore as PyQtCore
import sys

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

"""
first class
"""
#
# app = PyQtGui.QApplication(sys.argv)
# b = PyQtGui.QPushButton('Hello Kitty')
# b.show()
# app.connect(b, PyQtCore.SIGNAL('clicked()'), app, PyQtCore.SLOT('quit()'))
# app.exec_()

"""
second class
"""
# class Geometry(PyQtGui.QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.setWindowTitle("Geometry")
#
#         Label1 = PyQtGui.QLabel("x0:")
#         Label2 = PyQtGui.QLabel("y0:")
#         Label3 = PyQtGui.QLabel("frameGeometry():")
#         Label4 = PyQtGui.QLabel("pos():")
#         Label5 = PyQtGui.QLabel("geometry():")
#         Label6 = PyQtGui.QLabel("width():")
#         Label7 = PyQtGui.QLabel("height():")
#         Label8 = PyQtGui.QLabel("rect():")
#         Label9 = PyQtGui.QLabel("size():")
#
#         self.xLabel = PyQtGui.QLabel()
#         self.yLabel = PyQtGui.QLabel()
#         self.frameGeoLabel = PyQtGui.QLabel()
#         self.posLabel = PyQtGui.QLabel()
#         self.geoLabel = PyQtGui.QLabel()
#         self.widthLabel = PyQtGui.QLabel()
#         self.heightLabel = PyQtGui.QLabel()
#         self.rectLabel = PyQtGui.QLabel()
#         self.sizeLabel = PyQtGui.QLabel()
#
#         layout = PyQtGui.QGridLayout()
#         layout.addWidget(Label1, 0, 0)
#         layout.addWidget(self.xLabel, 0, 1)
#         layout.addWidget(Label2, 1, 0)
#         layout.addWidget(self.yLabel, 1, 1)
#         layout.addWidget(Label3, 2, 0)
#         layout.addWidget(self.frameGeoLabel, 2, 1)
#         layout.addWidget(Label4, 3, 0)
#         layout.addWidget(self.posLabel, 3, 1)
#         layout.addWidget(Label5, 4, 0)
#         layout.addWidget(self.geoLabel, 4, 1)
#         layout.addWidget(Label6, 5, 0)
#         layout.addWidget(self.widthLabel, 5, 1)
#         layout.addWidget(Label7, 6, 0)
#         layout.addWidget(self.heightLabel, 6, 1)
#         layout.addWidget(Label8, 7, 0)
#         layout.addWidget(self.rectLabel, 7, 1)
#         layout.addWidget(Label9, 8, 0)
#         layout.addWidget(self.sizeLabel, 8, 1)
#
#         self.setLayout(layout)
#
#         self.updateLabel()
#
#     def moveEvent(self, event):
#         self.updateLabel()
#
#     def resizeEvent(self, event):
#         self.updateLabel()
#
#     def updateLabel(self):
#         self.xLabel.setText(str(self.x()))
#         self.yLabel.setText(str(self.y()))
#         self.frameGeoLabel.setText(str(self.frameGeometry().x()) + "," +
#                                    str(self.frameGeometry().y()) + "," +
#                                    str(self.frameGeometry().width()) + "," +
#                                    str(self.frameGeometry().height()))
#
#         self.posLabel.setText(str(self.pos().x()) + "," +
#                               str(self.pos().y()))
#         self.geoLabel.setText(
#             "{0},{1},{2},{3}".format(str(self.geometry().x()), str(self.geometry().y()), str(self.geometry().width()),
#                                      str(self.geometry().height())))
#         self.widthLabel.setText(str(self.width()))
#         self.heightLabel.setText(str(self.height()))
#         self.rectLabel.setText(str(self.rect().x()) + "," +
#                                str(self.rect().y()) + "," +
#                                str(self.rect().width()) + "," +
#                                str(self.rect().height()))
#         self.sizeLabel.setText(str(self.size().width()) + "," +
#                                str(self.size().height()))
#
#
# app = PyQtGui.QApplication(sys.argv)
# form = Geometry()
# form.show()
# app.exec_()


"""
second class
"""
