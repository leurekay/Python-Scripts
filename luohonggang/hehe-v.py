# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:28:11 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
N=10
Low=0
High=2
Step=0.1
mc_step=0.05
md_step=0.05
v_step=0.05



def Ek(j,v,kx,ky):
    f1=j**2*v**2/2 
    +1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2
    cha=j**4*v**4/4
    
    return sqrt(f1+sqrt(cha))

def E(j,v):
    total=0
    for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
        for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
            total=total+Ek(j,v,kx,ky)
    return -1*total/N**2 +j*v**2

def get_order(j):
    temp=99999
    index=0
    for v in np.arange(0.4,0.8,v_step):   
        val=E(j,v)  
        print val,'j:',j,' v:',v
        if val<temp:
            temp=val
            index=v
    return index

Lx=np.arange(Low,High,Step)        

Lv=[]  
for j in Lx:

    Lv.append(get_order(j))
    print j
x=Lx
y=Lv    
plt.figure(figsize=(16,8))
plt.plot(x,y,label=".",color="blue",linewidth=2)
plt.xlabel("v")
plt.ylabel("E")
plt.title("E-v")
plt.ylim(-2,2)
plt.legend()
plt.show()