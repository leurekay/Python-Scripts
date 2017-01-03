# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:27:37 2016
给定j,遍历序参量mc,md,v,求得使能量最小的序参量
@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
N=8
Low=0.1
High=2.3
Step=0.05
mc_step=0.02
md_step=0.02
v_step=0.05

def Ek(j,mc,md,v,kx,ky):
    f1=j**2*(md**2+mc**2)/4 +j**2*v**2/2
    +1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2
    cha=4*(j**4*md**2*mc**2/16+j**4*md*mc*v**2/8+j**4*v**4/16)
    +j**2*mc**2*(1+ 4*cos(1.5*kx)*cos(ky*sqrt(3)/2)+4*(cos(ky*sqrt(3)/2))**2)
    
    return sqrt(f1+sqrt(cha))

def E(j,mc,md,v):
    total=0
    for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
        for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/N):
            total=total+Ek(j,mc,md,v,kx,ky)
    return -1*total/N**2 +(2*j*md*mc+j*v**2)

def get_order(j):
    temp=99999
    L=[]
    for mc in np.arange(0.01,0.52,mc_step):
        for md in np.arange(0.01,0.52,md_step):
            for v in np.arange(0.01,1,v_step):
                E_jj=E(j,mc,md,v)
                if E_jj<temp :
                    temp=E_jj
                    L=[mc,md,v]
    return L

Lx=np.arange(Low,High,Step)        
Lmc=[]  
Lmd=[]
Lv=[]  
for j in Lx:
    val=get_order(j)
    Lmc.append(val[0])
    Lmd.append(val[1])
    Lv.append(val[2])
    print j
x=Lx
y=Lv 
y1=Lmc
y2=Lmd   
plt.figure(figsize=(16,8))
plt.plot(x,y,label="v",color="blue",linewidth=2)
plt.plot(x,y1,label="mc",color="green",linewidth=2)
plt.plot(x,y2,label="md",color="red",linewidth=2)
plt.xlabel("v")
plt.ylabel("E")
plt.title("E-v")
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()