# -*- coding: utf-8 -*-
"""
Created on Mon May 09 15:56:37 2016
E关于v的方程，求E的极值
@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
N=20
Low=0.1
High=0.9
Step=0.0005

def Ek(v,kx,ky):
    f1=1.165**2/4/(1-v)*(0.25+0.09**2/(1-v))+1.165**2*v**2/2/(1-v)
    +1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2
    cha=4*(1.165**4*0.09**2/64/(1-v)**3+ 1.165**4*v**2*0.09/16/(1-v)**2.5+1.165**4*v**4/16/(1-v)**2)
    +1.165**2*0.09/(1-v)**1.5*(1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2)
    
    return sqrt(f1+sqrt(cha))

def E(v):
    total=0
    for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
        for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
            total=total+Ek(v,kx,ky)
    return -1*total/N**2+ 1.165*0.09/(1-v)+1.165*v**2/sqrt(1-v)
            
Lx=np.arange(Low,High,Step)        
Ly=[]    
for v in Lx:
    val=E(v)
    Ly.append(val)
    print val,v

x=Lx
y=Ly    
plt.figure(figsize=(16,8))
plt.plot(x,y,label=".",color="blue",linewidth=2)
plt.xlabel("v")
plt.ylabel("E")
plt.title("E-v")
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
