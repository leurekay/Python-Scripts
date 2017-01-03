# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:01:23 2016
ratio=<x'|psi>/<x|psi>=det(D')/det(D)=W[l][beta]
Ratio:skill
Ratio1:brute 
Ratio2:wrong

DysonRatio:用dyson方法计算hoping所产生的行列式比值，但并不涉及链式更新G

Ratio_exchange:直接计算自旋翻转前后两个行列式的比值
Ratio_exchange1:C，D电子跳到相反自旋，间接计算行列式比值
Ratio_exchange2:D电子跳到相同自旋C电子，C电子跳到相同自旋D电子，间接计算行列式比值

remark：Ratio_exchange和Ratio_exchange2偶尔会相差一个负号，但Ratio_exchange1和其他两个绝对不一样

把所有的返回值都置为实数

@author: aa
"""
from __future__ import division
import numpy as np
from mfh import Hamiltonian
import scipy
from configure import *

def Det(conf,L,j,mc,md,v,u):
    M=u[:,np.arange(0,L*L*4,1)]
    occupy_index=[]
    for i in range(np.size(conf)):
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]
    return np.linalg.det(D)

def G_and_Idx(conf,L,j,mc,md,v,u):
    u=u.T
    occupy_index=[]
    for i in range(np.size(conf)):
        if conf[0][i]!=0:
            occupy_index.append(i)
            
    M=u[np.arange(0,L*L*4,1),:]
    Ginv=M[:,occupy_index]
    G=np.linalg.inv(Ginv)
    u=u.T
    return G,occupy_index
    
def Ratio(conf,before,after,L,j,mc,md,v,u):  #before-th site to the after-th site
    #p1=Hamiltonian(L,j,mc,md,v)
    #u=p1.unitary
    #dia=p1.diagonal
    M=u[:,np.arange(0,L*L*4,1)]
    occupy_index=[]
    for i in range(np.size(conf)):
        if i==before:
            beta=len(occupy_index)    #beta :correspoding position in D matrix or the particle index
        if conf[0][i]!=0:
            occupy_index.append(i)
    D=M[occupy_index]
    W=np.dot(M,np.linalg.inv(D))
    #print W[after][beta]
    #W=(scipy.linalg.solve(D.T,M.T)).T
    #print W[after][beta]
    return W[after][beta].real

def Ratio1(conf,before,after,L,j,mc,md,v,u):  #before-th site to the after-th site
    M=u[:,np.arange(0,L*L*4,1)]
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
    ratio=det_new/det_old
    #print ratio
    #if ratio>9999999999:
     #   print conf,before,after
    return ratio.real
"""
def Ratio2(conf,before,after,L,j,mc,md,v,u):  #before-th site to the after-th site
    #p1=Hamiltonian(L,j,mc,md,v)
    #u=p1.unitary
    print type(u[0][0])
    #dia=p1.diagonal
    M=u[:,np.arange(0,L*L*4,1)]
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
    print ratio
    return ratio
"""
def Ratio_exchange(conf,cell,A_B,L,j,mc,md,v,u):
    #针对自旋翻转情形，直接计算行列式比值
    #cell表示第几个元胞
    #Lattice A:0
    #Lattice B:1
    det_old=Det(conf,L,j,mc,md,v,u)
    if A_B != 0 and A_B != 1:
        return "invalid"
    ele_up=cell*8+0+A_B
    ele_down=cell*8+2+A_B
    spin_up=cell*8+4+A_B
    spin_down=cell*8+6+A_B
    if conf[0][spin_up]==2 and conf[0][ele_up]==0 and conf[0][ele_down]==1:
        conf_temp=np.copy(conf)
        conf_temp[0][ele_up]=1
        conf_temp[0][ele_down]=0
        conf_temp[0][spin_up]=0
        conf_temp[0][spin_down]=2
        det_new=Det(conf_temp,L,j,mc,md,v,u)
        return (det_new/det_old).real
    elif conf[0][spin_down]==2 and conf[0][ele_up]==1 and conf[0][ele_down]==0:
        conf_temp=np.copy(conf)
        conf_temp[0][ele_up]=0
        conf_temp[0][ele_down]=1
        conf_temp[0][spin_up]=2
        conf_temp[0][spin_down]=0
        det_new=Det(conf_temp,L,j,mc,md,v,u)
        return (det_new/det_old).real
    else:
        return "invalid"
def Ratio_exchange1(conf,cell,A_B,L,j,mc,md,v,u):
    #针对自旋翻转情形，间接计算行列式比值,调用的是Ratio1
    if A_B != 0 and A_B != 1:
        return "invalid"
    ele_up=cell*8+0+A_B
    ele_down=cell*8+2+A_B
    spin_up=cell*8+4+A_B
    spin_down=cell*8+6+A_B
    if conf[0][spin_up]==2 and conf[0][ele_up]==0 and conf[0][ele_down]==1:
        conf_temp=np.copy(conf)
        conf_temp[0][spin_up]=0
        conf_temp[0][spin_down]=2
        #ratio1=Ratio1(conf,spin_up,spin_down,L,j,mc,md,v,u)
        #ratio2=Ratio1(conf_temp,ele_down,ele_up,L,j,mc,md,v,u)
        ratio1=DysonRatio(conf,spin_up,spin_down,L,j,mc,md,v,u)
        ratio2=DysonRatio(conf_temp,ele_down,ele_up,L,j,mc,md,v,u)
        
        return ratio1*ratio2
    elif conf[0][spin_down]==2 and conf[0][ele_up]==1 and conf[0][ele_down]==0:
        conf_temp=np.copy(conf)
        conf_temp[0][spin_up]=2
        conf_temp[0][spin_down]=0
        #ratio1=Ratio1(conf,spin_down,spin_up,L,j,mc,md,v,u)
        #ratio2=Ratio1(conf_temp,ele_up,ele_down,L,j,mc,md,v,u)
        ratio1=DysonRatio(conf,spin_down,spin_up,L,j,mc,md,v,u)
        ratio2=DysonRatio(conf_temp,ele_up,ele_down,L,j,mc,md,v,u)
        return ratio1*ratio2
        return ratio1*ratio2
    else:
        return "invalid"
def Ratio_exchange2(conf,cell,A_B,L,j,mc,md,v,u):
    #D电子跳到相同自旋C电子，C电子跳到相同自旋D电子
    if A_B != 0 and A_B != 1:
        return "invalid"
    ele_up=cell*8+0+A_B
    ele_down=cell*8+2+A_B
    spin_up=cell*8+4+A_B
    spin_down=cell*8+6+A_B
    if conf[0][spin_up]==2 and conf[0][ele_up]==0 and conf[0][ele_down]==1:
        conf_temp=np.copy(conf)
        conf_temp[0][spin_up]=0
        conf_temp[0][ele_up]=1
        #ratio1=Ratio1(conf,spin_up,spin_down,L,j,mc,md,v,u)
        #ratio2=Ratio1(conf_temp,ele_down,ele_up,L,j,mc,md,v,u)
        ratio1=DysonRatio(conf,spin_up,ele_up,L,j,mc,md,v,u)
        ratio2=DysonRatio(conf_temp,ele_down,spin_down,L,j,mc,md,v,u)
        return ratio1*ratio2
    elif conf[0][spin_down]==2 and conf[0][ele_up]==1 and conf[0][ele_down]==0:
        conf_temp=np.copy(conf)
        conf_temp[0][ele_down]=1
        conf_temp[0][spin_down]=0
        #ratio1=Ratio1(conf,spin_down,ele_down,L,j,mc,md,v,u)
        #ratio2=Ratio1(conf_temp,ele_up,spin_up,L,j,mc,md,v,u)
        ratio1=DysonRatio(conf,spin_down,ele_down,L,j,mc,md,v,u)
        ratio2=DysonRatio(conf_temp,ele_up,spin_up,L,j,mc,md,v,u)
        return ratio1*ratio2
    else:
        return "invalid"

def DysonRatio(conf,before,after,L,j,mc,md,v,u):
    u=np.conjugate(u.T)
    occupy_index=[]
    for i in range(np.size(conf)):
        if i==before:
            beta=len(occupy_index)    #beta :correspoding position in D matrix or the particle index
        if conf[0][i]!=0:
            occupy_index.append(i)
            
    M=u[np.arange(0,L*L*4,1),:]
    Ginv=M[:,occupy_index]
    SIGMA=M[:,before]-M[:,after]
    G=np.linalg.inv(Ginv)
    global GGinv
    GGinv=np.dot(G,Ginv)
    u=u.T
    return 1-np.dot(G[beta,:],SIGMA)


    


if __name__=='__main__' :
    L=2
    j=3
    mc=0.01
    md=0.07
    v=1.15
    before=8
    after=9
    p1=Hamiltonian(L,j,mc,md,v)
    u=p1.unitary
    #u=u.real
    dia=p1.diagonal
    conf_old=conf_initial(L)
    #conf_old=np.array([[1, 1, 1, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 1 ,1 ,1 ,1 ,2, 0, 0, 2]])        
    print "算行列式差分"
    print Det(conf_old,L,j,mc,md,v,u)
    
    print "-----------------------------"    
    
    conf_old=np.array([[1, 0, 1, 1, 2, 2, 0, 0, 1, 0, 1, 1, 2, 0, 0, 2, 0, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0 ,0 ,2]])
    #print Ratio(conf_old,0,25,L,j,mc,md,v,u)
    #print Ratio1(conf_old,0,25,L,j,mc,md,v,u)
    print "**********************"
    print Ratio_exchange(conf_old,before,after,L,j,mc,md,v,u)
    print Ratio_exchange1(conf_old,before,after,L,j,mc,md,v,u)
    print Ratio_exchange2(conf_old,before,after,L,j,mc,md,v,u)
    print "----------------------"
    print Ratio(conf_old,before,after,L,j,mc,md,v,u)
    print Ratio1(conf_old,before,after,L,j,mc,md,v,u)
    print DysonRatio(conf_old,before,after,L,j,mc,md,v,u)
    
    