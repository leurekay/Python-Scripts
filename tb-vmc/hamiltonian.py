# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:50:09 2016

@author: aa
"""
from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 

def up(i,L):
    if i//L==0:
        return i+L*(L-1)
    else:
        return i-L
def down(i,L):
    if i//L==L-1:
        return i-L*(L-1)
    else:
        return i+L
def left(i,L):
    if i%L==0:
        return i+L-1
    else:
        return i-1
def right(i,L):
    if i%L==L-1:
        return i+1-L
    else:
        return i+1

def H(L):
    h=np.zeros((2*L**2,2*L**2),dtype='float')
    for i in range(L**2):
        h[i][up(i,L)]=h[i][down(i,L)]=h[i][left(i,L)]=h[i][right(i,L)]=-1
        h[i+L**2][up(i,L)+L**2]=h[i+L**2][down(i,L)+L**2]=h[i+L**2][left(i,L)+L**2]=h[i+L**2][right(i,L)+L**2]=-1
    dia,u=np.linalg.eig(h)
    idx = dia.argsort() 
    dia = dia[idx]
    u = u[:,idx]
    return h,dia,u

if __name__=='__main__':
    L=12
    h,dia,u=H(L)     
    E_total=0
    for i in range(L**2):
        E_total=E_total+dia[i]
    E_site=E_total/L**2