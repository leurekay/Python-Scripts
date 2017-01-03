# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:18:00 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt


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
        h=np.zeros((8*L**2,8*L**2))
        for i in range(L**2):
            h[i*8][i*8+1]=h[i*8][8*left(i)+1]=h[i*8][8*down(i)+1]=-1
            h[i*8+1][i*8]=h[8*left(i)+1][i*8]=h[8*down(i)+1][i*8]=-1
            h[i*8+2][i*8+3]=h[i*8+2][8*left(i)+3]=h[i*8+2][8*down(i)+3]=-1
            h[i*8+3][i*8+2]=h[8*left(i)+3][i*8+2]=h[8*down(i)+3][i*8+2]=-1

            h[i*8+6][i*8+2]=h[i*8+0][i*8+4]=h[i*8+4][i*8+0]=h[i*8+2][i*8+6]=j*v/2
            h[i*8+7][i*8+3]=h[i*8+1][i*8+5]=h[i*8+5][i*8+1]=h[i*8+3][i*8+7]=j*v/2

            h[i*8+4][i*8+4]=h[i*8+6][i*8+6]=-j*mc/2
            h[i*8+0][i*8+0]=h[i*8+2][i*8+2]=j*md/2
            h[i*8+5][i*8+5]=h[i*8+7][i*8+7]=j*mc/2
            h[i*8+1][i*8+1]=h[i*8+3][i*8+3]=-j*md/2
        
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
        return self.new_eigen[0].real
    @property
    def unitary(self):
        return self.new_eigen[1].real
        
if __name__=='__main__' :
    L=2
    j=2.3
    mc=0.2
    md=0.2
    v=0.6
    p1=Hamiltonian(L,j,mc,md,v)
    dia=p1.diagonal
    u=p1.unitary
    for m in range(8*L**2):
        total=0
        for n in range(8*L**2):
            total=total+u[n][m]*u[n][3]
        print total   

