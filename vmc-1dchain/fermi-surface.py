# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:46:25 2016
2D square lattice,plot the fermi surface by the filling
@author: aa
"""
import numpy as np
from math import *
import matplotlib  
import matplotlib.pyplot as plt 
L=200
N=L**2
fill=1.2
kx_range=np.arange(-pi,pi,2*pi/L)
ky_range=np.arange(-pi,pi,2*pi/L)

Ekxky=np.zeros((3,L*L),"float")
i=0
for kx in kx_range:
    for ky in ky_range:
        Ekxky[0][i]=-2*cos(kx)-2*cos(ky)
        Ekxky[1][i]=kx
        Ekxky[2][i]=ky
        i=i+1
E_arr=Ekxky[0,:]
inx=E_arr.argsort()
aa=Ekxky[:,inx]

#f1 = plt.figure(1)  
#plt.subplot(211) 
plt.figure(figsize=(8,8))
plt.xlim(xmax=pi,xmin=-pi)
plt.ylim(ymax=pi,ymin=-pi)
plt.scatter(aa[1,0:N*fill/2],aa[2,0:N*fill/2])  