# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 19:43:30 2016
E_loc2错误
@author: aa
"""
from __future__ import division
from math import *
import numpy as np
import random,time,copy
from hamiltonian import *
from slater import *
from configuration import conf_initial


def E_loc2(conf,L,u):  #ratio of two determinant brutely
    box=[]
    box1=[]
    for i in range(L):
        if conf[0][i]==1:
            if conf[0][left(i,L)]==0:
                conf_temp=copy.copy(conf)
                conf_temp[0][left(i,L)]=1
                conf_temp[0][i]=0
                box.append(conf_temp)
            if conf[0][right(i,L)]==0:
                conf_temp=copy.copy(conf)
                conf_temp[0][right(i,L)]=1
                conf_temp[0][i]=0
                box.append(conf_temp)
            
        if conf[0][i+L]==1:
            if conf[0][left(i,L)+L]==0:
                conf_temp=copy.copy(conf)
                conf_temp[0][left(i,L)+L]=1
                conf_temp[0][i+L]=0
                box.append(conf_temp)
            if conf[0][right(i,L)+L]==0:
                conf_temp=copy.copy(conf)
                conf_temp[0][right(i,L)+L]=1
                conf_temp[0][i+L]=0
                box.append(conf_temp)
    den=Det(conf,L,u)
    for i in box:
        box1.append(Det(i,L,u)/den)
        #print Det(i,L,u)/den
    return -sum(box1)

def E_loc(conf,L,u):  #using skills to compute the ratio 
    box=[]
    for i in range(L):
        if conf[0][i]==1:
            if conf[0][left(i,L)]==0:
                box.append(Ratio(conf,i,left(i,L),L,u)[0])
            if conf[0][right(i,L)]==0:
                box.append(Ratio(conf,i,right(i,L),L,u)[0])
            
        if conf[0][i+L]==1:
            if conf[0][left(i,L)+L]==0:
                box.append(Ratio(conf,i+L,left(i,L)+L,L,u)[0])
            if conf[0][right(i,L)+L]==0:
                box.append(Ratio(conf,i+L,right(i,L)+L,L,u)[0])
                
    return -sum(box)
    
def E_loc1(conf,L,u):  #ratio of two determinant brutely
    box=[]
    for i in range(L):
        if conf[0][i]==1:
            if conf[0][left(i,L)]==0:
                box.append(Ratio1(conf,i,left(i,L),L,u))
            if conf[0][right(i,L)]==0:
                box.append(Ratio1(conf,i,right(i,L),L,u))
            
        if conf[0][i+L]==1:
            if conf[0][left(i,L)+L]==0:
                box.append(Ratio1(conf,i+L,left(i,L)+L,L,u))
            if conf[0][right(i,L)+L]==0:
                box.append(Ratio1(conf,i+L,right(i,L)+L,L,u))
    return -sum(box)


if __name__=='__main__' : 
    L=32
    N_up=16
    h,dia,u=H(L)

    conf=conf_initial(L,N_up)
    bb=E_loc(conf,L,u)
    bb1=E_loc1(conf,L,u)