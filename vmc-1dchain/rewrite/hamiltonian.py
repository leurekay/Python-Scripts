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


def left(i,L):
    if i==0:
        return L-1
    else:
        return i-1
def right(i,L):
    if i==L-1:
        return 0
    else:
        return i+1

def H(L):
    h=np.zeros((2*L,2*L),dtype='float')
    for i in range(L):
        h[i][left(i,L)]=h[i][right(i,L)]=-1
        h[i+L][left(i,L)+L]=h[i+L][right(i,L)+L]=-1
    dia,u=np.linalg.eig(h)
    idx = dia.argsort() 
    dia = dia[idx]
    u = u[:,idx]
    return h,dia,u

if __name__=='__main__':
    L=6
    h,dia,u=H(L)     
    E_total=0
    for i in range(L):
        E_total=E_total+dia[i]
    E_site=E_total/L