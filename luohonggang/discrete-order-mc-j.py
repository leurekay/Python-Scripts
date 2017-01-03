# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:57:10 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
N=100
Low=0
High=3
Step=0.02

f=lambda j,kx,ky:j/sqrt(j**2+16*(1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2))
    
    
def mc_j(j):
    
    total=0
    for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
        for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
            total=total+f(j,kx,ky)
    return total/2/N**2
            
Lx=np.arange(Low,High,Step)        
Ly=[]    
for j in Lx:
    val=mc_j(j)
    Ly.append(val)
    print val,j

x=Lx
y=Ly
z=Lx*(np.sqrt(Lx**2/4+4*2.33**2)-Lx/2)/8/2.33**2 
w=0.18/2.33*Lx  
plt.figure(figsize=(16,8))
plt.plot(x,y,color="blue",linewidth=1,label="discrete")
plt.plot(x,z,"r",label="continue",linewidth=1)
plt.plot(x,w,"g",label="linear approximate",linewidth=1)
plt.xlabel("v")
plt.ylabel("E")
plt.title("E-v")
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()