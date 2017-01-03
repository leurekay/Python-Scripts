# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:59:42 2016

@author: aa
"""

from __future__ import division
import numpy as np
from hamiltonian import H
import scipy
from configuration import conf_initial

def Ratio(conf,before,after,L):  #before-th site to the after-th site

    h,dia,u=H(L)
    M=u[:,np.arange(0,L*L,1)]
    occupy_index=[]
    for i in range(np.size(conf)):
        if i==before:
            beta=len(occupy_index)    #beta :correspoding position in D matrix or the particle index
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]
    #print "##########",np.linalg.det(D)
    W=np.dot(M,np.linalg.inv(D))
    #W=(scipy.linalg.solve(D.T,M.T)).T
    return [W[after][beta],occupy_index,W,u,dia]


if __name__=='__main__' :
    L=8
    conf=conf_initial(L)
    
    print Ratio(conf,1,2,L)[0]