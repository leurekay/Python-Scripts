# -*- coding: utf-8 -*-
"""
Created on Mon May 09 12:36:41 2016

@author: aa
"""


from __future__ import division
from math import *
import numpy as np

N=100

def Ek(j,kx,ky):
    f1=j**2*(0.25+j**2*0.11**2/2.33**2)/4+j**2*(1-2.33**2/4/j**2)**2/2
    +1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2
    cha=4*(j**6*0.11**2/64/2.33**2+j**5*0.11/16/2.33*(1-2.33**2/4/j**2)**2+j**4*(1-2.33/4/j**2)**4/16)
    +j**4*0.11**2/2.33**2*(1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2)
    return sqrt(f1+sqrt(cha))

def E(j):
    total=0
    for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
        for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
            total=total+Ek(j,kx,ky)
    return -1*total/N**2 +2*j**2*0.5*0.11/2.33+ j*(1-2.33**2/4/j**2)**2
            
        
    
Lx=np.arange(0.1,2.5,0.05)        
Ly=[]    
for j in Lx:
    val=E(j)
    Ly.append(val)
    print val,j

x=Lx
y=Ly    
plt.figure(figsize=(24,12))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
