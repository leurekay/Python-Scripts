# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 13:40:49 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from hamiltonian import order

L=10
mc=0.2
md=0.2
v=0.5
j_start=0.01
j_stop=3
j_step=0.01
J=np.arange(j_start,j_stop,j_step)

def get_order(L,j):
    mc=0.01
    md=0.01
    v=0.83
    while True:
        new_mc,new_md,new_v=order(L,j,mc,md,v)
        if abs(mc-new_mc)<0.001 and abs(md-new_md)<0.001 and abs(v-new_v)<0.001:
            break
        else:
            mc=new_mc
            md=new_md
            v=new_v
    return [mc,md,v]
    
L_mc=[]
L_md=[]
L_v=[]
for j in J:
    mc,md,v=get_order(L,j)
    L_mc.append(mc)
    L_md.append(md)
    L_v.append(v)
    print 'j=',j, 'mc:',mc,'md:',md, 'v:',v
    
x=J
y1=L_mc
y2=L_md
y3=L_v
plt.figure(figsize=(16,8))
plt.plot(x,y1,color="blue",linewidth=1,label="mc")
plt.plot(x,y2,"r",label="md",linewidth=1)
plt.plot(x,y3,"g",label="v",linewidth=1)
plt.xlabel("j")
plt.ylabel("order")
plt.title("cell:%d*%d"%(L,L))
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
