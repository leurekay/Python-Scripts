# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 20:18:24 2016
make a big mistake!!!
the range of kx should be [-pi/3,pi/3],
rather than [-pi/sqrt(3),pi/sqrt(3)].

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from hamiltonian2 import order

L=12
mc=0.1
md=0.1
v=0.4
j_start=0.1
j_stop=3
j_step=0.02
J=np.arange(j_start,j_stop,j_step)

def get_order(L,j):
    mc=0.01
    md=0.01
    v=0.83
    while True:
        new_mc,new_md,new_v,new_E=order(L,j,mc,md,v)
        if abs(mc-new_mc)<0.0001 and abs(md-new_md)<0.0001 and abs(v-new_v)<0.0001:
            break
        else:
            mc=new_mc
            md=new_md
            v=new_v
            E=new_E
    return [mc,md,v,E]
    
L_mc=[]
L_md=[]
L_v=[]
L_E=[]
for j in J:
    mc,md,v,E=get_order(L,j)
    L_mc.append(abs(mc))
    L_md.append(abs(md))
    L_v.append(v)
    L_E.append(E+v**2+2*mc*md)
    print 'j=',j, 'mc:',mc,'md:',md, 'v:',v,'E:',E
    
x=J
y1=L_mc
y2=L_md
y3=L_v
y4=L_E
plt.figure(figsize=(20,10))
plt.plot(x,y1,"bo-",label="mc",linewidth=1.5)
plt.plot(x,y2,"r^-",label="md",linewidth=1.5)
plt.plot(x,y3,"g*-",label="v",linewidth=1.5)
#plt.plot(x,y4,"y",label="E",linewidth=1)
plt.xlabel("j",fontsize= 'xx-large')
plt.ylabel("order", fontsize= 'xx-large')
plt.title("cell:%d*%d ,j_step:%.2f"%(L,L,j_step),fontsize= 'xx-large')
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

plt.figure(figsize=(20,10))
plt.plot(x,y4,"bo-",label="E",linewidth=1.5)
plt.xlabel("j",fontsize= 'xx-large')
plt.ylabel("E",fontsize= 'xx-large')
plt.title("cell:%d*%d"%(L,L),fontsize= 'xx-large')