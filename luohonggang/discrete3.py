# -*- coding: utf-8 -*-
"""
Created on Mon May 09 18:23:00 2016
把其他参数表示为关于序参量mc的函数，
然后求能量关于mc的极值点
@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
cj=2.33/0.18
cv=0.25*0.18**2
N=50
Low=0
High=0.5
Step=0.001
f=lambda mc:(np.exp(mc/3/0.11)-np.exp(-mc/3/0.11))/(np.exp(mc/3/0.11)+np.exp(-mc/3/0.11))

def Ek(mc,kx,ky):
    f1=cj**2*mc**2*(0.25+mc**2)/4 +cj**2*mc**2*f(mc)**2/2
    +1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2
    cha=4*(cj**4*mc**6/64 +cj**4*mc**5*f(mc)**2/16 +cj**4*mc**4*f(mc)**4/16)
    +cj**2*mc**4*(1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2)
    return sqrt(f1+sqrt(cha))

def E(mc):
    total=0
    for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
        for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
            total=total+Ek(mc,kx,ky)
    return -1*total/N**2+ cj*mc*(mc+f(mc)**2)
            
Lx=np.arange(Low,High,Step)        
Ly=[]    
for mc in Lx:
    val=E(mc)
    Ly.append(val)
    print val,mc

x=Lx
y=Ly    
plt.figure(figsize=(16,8))
plt.plot(x,y,label=".",color="blue",linewidth=2)
plt.xlabel("mc")
plt.ylabel("E")
plt.title("E-mc")
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()