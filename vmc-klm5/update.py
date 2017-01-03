# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 15:49:55 2016

@author: aa
"""

from __future__ import division
import random,copy,time
import numpy as np
from bound import *
from configure import conf_initial
from mfh import Hamiltonian
from slater import *
from observable import *

def Dyson_update(G,conf,before,after,L,j,mc,md,v,u):
    u=u.T
    occupy_index=[]
    for i in range(np.size(conf)):
        if i==before:
            beta=len(occupy_index)    #beta :correspoding position in D matrix or the particle index
        if conf[0][i]!=0:
            occupy_index.append(i)
            
    M=u[np.arange(0,L*L*4,1),:]
    SIGMA=M[:,before]-M[:,after]
    den=1-np.dot(G[beta,:],SIGMA)
    G=G+np.dot(G,np.dot(SIGMA,G[beta,:]))/den
    return den,G
def f():
    x,y=random.randrange(0,3),random.randrange(0,3)
    A[x][y]+=1
    
    
    
    
if __name__== "__main__":
    L=2
    j=3
    mc=0.01
    md=0.05
    v=1.95
    Nwarmup=10000
    Nstep=10000
    p1=Hamiltonian(L,j,mc,md,v)
    u=p1.unitary
    #u=u.real
    dia=p1.diagonal
    conf_old=conf_initial(L)
    ratio,G=DysonRatio(conf_old,67,20,L,j,mc,md,v,u)
    A=np.zeros((4,4))
    f()

    