# -*- coding: utf-8 -*-
"""
Created on Sat Nov 05 18:38:56 2016

@author: aa
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.2)
Y = np.arange(-5, 5, 0.2)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
Z=2*np.exp(-2*(X-2)**2-Y**2)+np.exp(-2*(X+0)**2-Y**2)+0.5*np.exp(-2*(X+1)**2-Y**2)+np.exp(-2*(X+2)**2-Y**2)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()