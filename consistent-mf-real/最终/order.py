# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 11:40:49 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
from  Hamiltonian import Hamiltonian

def get_mc(u):
    total=0
    ut=u.transpose()
    ud=np.conjugate(ut)
    for i in range(L**2):
        for j in range(4*L**2):
            total=total+u[i*8+2][j]*ud[j][i*8+2]-u[i*8+0][j]*ud[j][i*8+0]
    return total/(L**2)/2        
def get_md(u):
    total=0
    ut=u.transpose()
    ud=np.conjugate(ut)
    for i in range(L**2):
        for j in range(4*L**2):
            total=total+u[i*8+4][j]*ud[j][i*8+4]-u[i*8+6][j]*ud[j][i*8+6]
    return total/(L**2)/2
def get_v(u):
    total=0
    ut=u.transpose()
    ud=np.conjugate(ut)
    for i in range(L**2):
        for j in range(4*L**2):
            total=total- u[i*8+0][j]*ud[j][i*8+4]- u[i*8+6][j]*ud[j][i*8+2]
    return total/(L**2)
def order(j):
    mc=0.1
    md=0.1
    v=0.1
    while True:
        p1=Hamiltonian(L,j,mc,md,v)
        u=p1.unitary
        new_mc=get_mc(u)
        new_md=get_md(u)
        new_v=get_v(u)
        if abs(mc-new_mc)<0.003 and abs(md-new_md)<0.003 and abs(v-new_v)<0.003:
            break
        else:
            mc=new_mc
            md=new_md
            v=new_v
    print 'j=',j,'mc:',new_mc,'md:',new_md,'v:',new_v

    return [new_mc,new_md,new_v]

L=10
j_start=2.2
j_stop=2.4
j_step=0.01

J=np.arange(j_start,j_stop,j_step)

L_mc=[]
L_md=[]
L_v=[]
for j in J:
    #print 'computing.......now,j='
    mc,md,v=order(j)
    L_mc.append(mc)
    L_md.append(md)
    L_v.append(v)
    
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
#plt.savefig('a.png',dpi=400)