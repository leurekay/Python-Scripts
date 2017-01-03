# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:01:23 2016
ratio=<x'|psi>/<x|psi>=det(D')/det(D)=W[l][beta]

@author: aa
"""
from __future__ import division
import numpy as np
from mfh import Hamiltonian

def Ratio(conf,before,after,L,j,mc,md,v):  #before-th site to the after-th site
    p1=Hamiltonian(L,j,mc,md,v)
    u=p1.unitary
    M=u[:,np.arange(0,L*L*4,1)]
    occupy_index=[]
    for i in range(np.size(conf)):
        if i==before:
            beta=len(occupy_index)    #beta :correspoding position in D matrix or the particle index
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]
    W=np.dot(M,np.linalg.inv(D))
    return W[after][beta]


if __name__=='__main__' :
    L=2
    j=1.5
    mc=0.2
    md=0.6
    v=0.4
    conf_old=np.array([[1, 0, 1, 0, 0, 0, 2, 2, 0, 1, 1, 0, 0, 2, 2, 0, 0, 0, 1, 1, 2, 2,
        0, 0, 0, 1, 1, 0, 2, 0, 0, 2]])
    conf_new=np.array([[1, 0, 1, 1, 2, 0, 0, 2, 0, 0, 1, 0, 2, 0, 0, 2, 0, 1, 1, 1, 2, 2,
        0, 0, 0, 0, 0, 1, 0, 0, 2, 2]])
    print ratio(conf_new,12,19,L,j,mc,md,v)