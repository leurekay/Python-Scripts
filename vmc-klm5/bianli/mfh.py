# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:52:47 2016
mean-field hamiltonian
input:L,j,mc,md,v
output:Class, unitary matrix....

in each cell,corresponding is Cia
@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 
class Hamiltonian(object):
    def __init__(self,L,j,mc,md,v):
        self.L=L
        self.j=j
        self.mc=mc
        self.md=md
        self.v=v
    @property
    def mat(self):
        L=self.L
        j=self.j
        mc=self.mc
        md=self.md
        v=self.v
        down=lambda i:(i+L)%(L**2)
        left=lambda i:L*(i//L-(i-1)//L)+i-1
        h=np.zeros((8*L**2,8*L**2),dtype='float')
        for i in range(L**2):
            h[i*8][i*8+1]=h[i*8][8*left(i)+1]=h[i*8][8*down(i)+1]=-1
            h[i*8+1][i*8]=h[8*left(i)+1][i*8]=h[8*down(i)+1][i*8]=-1
            h[i*8+2][i*8+3]=h[i*8+2][8*left(i)+3]=h[i*8+2][8*down(i)+3]=-1
            h[i*8+3][i*8+2]=h[8*left(i)+3][i*8+2]=h[8*down(i)+3][i*8+2]=-1

            h[i*8+6][i*8+2]=h[i*8+0][i*8+4]=h[i*8+4][i*8+0]=h[i*8+2][i*8+6]=j*v/2
            h[i*8+7][i*8+3]=h[i*8+1][i*8+5]=h[i*8+5][i*8+1]=h[i*8+3][i*8+7]=j*v/2

            h[i*8+4][i*8+4]=h[i*8+7][i*8+7]=-j*mc/2
            h[i*8+0][i*8+0]=h[i*8+3][i*8+3]=j*md/2
            h[i*8+5][i*8+5]=h[i*8+6][i*8+6]=j*mc/2
            h[i*8+1][i*8+1]=h[i*8+2][i*8+2]=-j*md/2
        
        return h
    @property
    def new_eigen(self):
        values,vectors=np.linalg.eig(self.mat)

        idx = values.argsort() 
        values = values[idx]
        vectors = vectors[:,idx]
        return [values,vectors]
    @property
    def diagonal(self):
        return self.new_eigen[0]
    @property
    def unitary(self):
        return self.new_eigen[1]



def V_mc(L,j,mc,md,v):
    down=lambda i:(i+L)%(L**2)
    left=lambda i:L*(i//L-(i-1)//L)+i-1
    h=np.zeros((8*L**2,8*L**2),dtype='complex')
    for i in range(L**2):
        h[i*8+4][i*8+4]=h[i*8+7][i*8+7]=-j*mc/20
        h[i*8+5][i*8+5]=h[i*8+6][i*8+6]=j*mc/20
    return h
def V_md(L,j,mc,md,v):
    down=lambda i:(i+L)%(L**2)
    left=lambda i:L*(i//L-(i-1)//L)+i-1
    h=np.zeros((8*L**2,8*L**2),dtype='complex')
    for i in range(L**2):
        h[i*8+0][i*8+0]=h[i*8+3][i*8+3]=j*md/20
        h[i*8+1][i*8+1]=h[i*8+2][i*8+2]=-j*md/20
    return h
def V_v(L,j,mc,md,v):
    down=lambda i:(i+L)%(L**2)
    left=lambda i:L*(i//L-(i-1)//L)+i-1
    h=np.zeros((8*L**2,8*L**2),dtype='complex')
    for i in range(L**2):
        h[i*8+6][i*8+2]=h[i*8+0][i*8+4]=h[i*8+4][i*8+0]=h[i*8+2][i*8+6]=j*v/20
        h[i*8+7][i*8+3]=h[i*8+1][i*8+5]=h[i*8+5][i*8+1]=h[i*8+3][i*8+7]=j*v/20
    return h 
if __name__=='__main__' :
    L=2
    j=1.7
    mc=0.2
    md=0.3
    v=0.8
    p1=Hamiltonian(L,j,mc,md,v)
    H=p1.mat
    dia=p1.diagonal
    u=p1.unitary
    u_real=u.real
    ut=u_real.transpose()
    ud=np.conjugate(u.transpose())
    a=np.dot(ut,np.dot(H,u))
    b=np.dot(ut,u_real)
    c=np.dot(ud,u)
    uT=u.T
    d=np.dot(u,uT)