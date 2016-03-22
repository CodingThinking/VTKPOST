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

"""
first class
"""

app = PyQtGui.QApplication(sys.argv)
b = PyQtGui.QPushButton('Hello Kitty')
b.show()
app.connect(b,PyQtCore.SIGNAL('clicked()'),app,PyQtCore.SLOT('quit()'))
app.exec_()


"""

"""