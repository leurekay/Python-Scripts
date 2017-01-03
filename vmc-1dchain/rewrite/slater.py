# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:59:42 2016
Ratio2是错误的，会导致负符号
@author: aa
"""

from __future__ import division
import numpy as np
from hamiltonian import H
import scipy
from configuration import conf_initial

def Ratio(conf,before,after,L,u):  #before-th site to the after-th site
    I=np.identity(L)
    #h,dia,u=H(L)
    M=u[:,np.arange(0,L,1)]
    occupy_index=[]
    for i in range(np.size(conf)):
        if i==before:
            beta=len(occupy_index)    #beta :correspoding position in D matrix or the particle index
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]+0.00000000001*I
    #D=M[occupy_index]
    #print "##########",np.linalg.det(D)
    W=np.dot(M,np.linalg.inv(D))
    #print W[after][beta]
    
    W=(scipy.linalg.solve(D.T,M.T)).T
    #print W[after][beta]
    return [W[after][beta],occupy_index]

def Ratio2(conf,before,after,L,u):  #before-th site to the after-th site
    #h,dia,u=H(L)
    M=u[:,np.arange(0,L,1)]
    occupy_index=[]
    for i in range(np.size(conf)):       
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]
    
    conf[0][after]=conf[0][before]
    conf[0][before]=0
    occupy_index=[]
    for i in range(np.size(conf)):
        if conf[0][i]!=0:
            occupy_index.append(i)
    D1=M[occupy_index]
    ratio=np.linalg.det(D1)/np.linalg.det(D)
    #print ratio
    return [ratio,0,0,0,0]

def Ratio1(conf,before,after,L,u):
    M=u[:,np.arange(0,L,1)]
    occupy_index=[]
    for i in range(np.size(conf)):
        if i==before:
            beta=len(occupy_index)    #beta :correspoding position in D matrix or the particle index
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]
    det_old=np.linalg.det(D)
    D[beta,:]=M[after,:]
    det_new=np.linalg.det(D)
    print det_old,det_new
    return det_new/det_old

def Det(conf,L,u):
    #h,dia,u=H(L)
    M=u[:,np.arange(0,L,1)]
    occupy_index=[]
    for i in range(np.size(conf)):       
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]
    return np.linalg.det(D)
    

if __name__=='__main__' :
    L=32
    h,dia,u=H(L)
    conf=conf_initial(L,16)
    #conf=np.array([[1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1]])  
    #print Ratio(conf,15,8,L,u)
    print Ratio1(conf,3,4,L,u)
    #print Ratio2(conf,15,8,L,u)