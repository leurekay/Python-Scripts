# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:01:20 2016

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
    for i in range(L**2):
        for j in range(4*L**2):
            total=total+u[i*8+2][j]*ut[j][i*8+2]-u[i*8+0][j]*ut[j][i*8+0]
    return total/(L**2)/2        
def get_md(u):
    total=0
    ut=u.transpose()
    for i in range(L**2):
        for j in range(4*L**2):
            total=total+u[i*8+4][j]*ut[j][i*8+4]-u[i*8+6][j]*ut[j][i*8+6]
    return total/(L**2)/2
def get_v(u):
    total=0
    ut=u.transpose()
    for i in range(L**2):
        for j in range(4*L**2):
            total=total- u[i*8+0][j]*ut[j][i*8+4]- u[i*8+6][j]*ut[j][i*8+2]
    return total/(L**2)
            
L=8
j=2.8
mc=0.1
md=0.1
v=0.1
flag=0
while True:
    flag=flag+1
    print flag,'mc:',mc,'md:',md, 'v:',v
    p1=Hamiltonian(L,j,mc,md,v)
    u=p1.unitary
    new_mc=get_mc(u)
    new_md=get_md(u)
    new_v=get_v(u)
    if abs(mc-new_mc)<0.0008 and abs(md-new_md)<0.0008 and abs(v-new_v)<0.001:
        break
    else:
        mc=new_mc
        md=new_md
        v=new_v
print new_mc
print new_md
print new_v