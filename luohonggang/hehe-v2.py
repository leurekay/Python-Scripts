# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:49:44 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
N=200
Low=0
High=2
Step=0.1
mc_step=0.05
md_step=0.05
v_step=0.05
j=1.2


def Ek(v,kx,ky):
    f1=j**2*v**2/2 
    +1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2
    cha=j**4*v**4/4
    
    return sqrt(f1+sqrt(cha))

def E(v):
    total=0
    for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
        for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
            total=total+Ek(v,kx,ky)
    return -1*total/N**2 +j*v**2



Lv=np.arange(Low,High,Step)        
Ev=[]
for v in Lv:

    Ev.append(E(v))
    
x=Lv
y=Ev   
plt.figure(figsize=(16,8))
plt.plot(x,y,label=".",color="blue",linewidth=2)
plt.xlabel("v")
plt.ylabel("E")
plt.title("E-v")
plt.ylim(-2,2)
plt.legend()
plt.show()