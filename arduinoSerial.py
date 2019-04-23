#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:39:41 2019

@author: zackghalayini
"""


"""
Task 1
"""
#import serial
#import matplotlib.pyplot as plt
#
#ser = serial.Serial("/dev/cu.usbmodem14201",9600)
#n = 0
#dataLst = []
#while n < 500:
#    print (ser.readline())
#    dataPoint = ser.readline()
#    dataPoint = int(dataPoint)
#    dataLst.append(dataPoint)
#    n+=1
#
#ser.close()
#
#plt.plot(dataLst)
#plt.show()
#f = open("serialData.dat","w")
#f.write(str(dataLst))
#f.close()
#

"""
Task 2
"""
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import PlotWidget
import numpy as np

x = np.array([1,2,3])
y = np.array([1,2,3])
pg.setConfigOption('background','w')
penn = pg.mkPen('k',width = 2,style = QtCore.Qt.SolidLine)
p1 = pg.plot(x,y,pen = penn,title = 'The first pyqtgraph plot',symbol = 't',symbolSize = 20)
p1.setXRange(0,4)
p1.setYRange(0,4)
p1.setLabel('left','Voltage','V')
p1.setLabel('bottom','Time','s')
