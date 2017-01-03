# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:26:07 2016

@author: aa
"""
from __future__ import division
from math import *
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
kx = np.arange(-2*pi/3,2*pi/3, 0.2)
ky = np.arange(-2*pi/3,2*pi/3, 0.2)
kx,ky = np.meshgrid(kx, ky)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
#Z=2*np.exp(-2*(X-2)**2-Y**2)+np.exp(-2*(X+0)**2-Y**2)+0.5*np.exp(-2*(X+1)**2-Y**2)+np.exp(-2*(X+2)**2-Y**2)
Ekxky=1+4*np.cos(1.5*kx)*np.cos(0.5*ky*sqrt(3)+4*np.cos(ky*sqrt(3)/2)**2)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(kx, ky, Ekxky, rstride=1, cstride=1, cmap='rainbow')
plt.show()
#plt.savefig(dpi=(20,20),a")
plt.contour(kx, ky, Ekxky)