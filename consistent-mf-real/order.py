# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:44:21 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
from  Hamiltonian import Hamiltonian

L=5
j=2.1

def get_mc(u):
    total=0
    ut=u.transpose()
    for i in range(L**2):
        for j in range(4*L**2):
            total=total+abs(u[j][i*8+2]*ut[i*8+2][j])-abs(u[j][i*8+0]*ut[i*8+0][j])
    return total/(L**2)/2        
def get_md(u):
    total=0
    ut=u.transpose()
    for i in range(L**2):
        for j in range(4*L**2):
            total=total+abs(u[j][i*8+4]*ut[i*8+4][j])-abs(u[j][i*8+6]*ut[i*8+6][j])
    return total/(L**2)/2
def get_v(u):
    total=0
    ut=u.transpose()
    for i in range(L**2):
        for j in range(4*L**2):
            total=total- u[j][i*8+0]*ut[i*8+4][j]- u[j][i*8+1]*ut[i*8+5][j]- u[j][i*8+6]*ut[i*8+2][j]- u[j][i*8+7]*ut[i*8+3][j]
    return total/(2*L**2)/2
            

mc=-0.15035417051
md=-0.174375389534
v=0.0982684513819
flag=0
while True:
    flag=flag+1
    print flag,'mc:',mc,'md:',md, 'v:',v
    p1=Hamiltonian(L,j,mc,md,v)
    u=p1.unitary
    new_mc=get_mc(u)
    new_md=get_md(u)
    new_v=get_v(u)
    if abs(mc-new_mc)<0.002 and abs(md-new_md)<0.002 and abs(v-new_v)<0.002:
        break
    else:
        mc=new_mc
        md=new_md
        v=new_v
print new_mc
print new_md
print new_v
    


