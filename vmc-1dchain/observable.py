# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 19:43:30 2016

@author: aa
"""
from __future__ import division
from math import *
import numpy as np
import random,time,copy
from hamiltonian import *
from slater import *
from configuration import conf_initial


def E_loc1(conf,L):   #compute the ratio of two determinant directly
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
    den=Det(conf,L)
    for i in box:
        box1.append(Det(i,L)/den)
    return -sum(box1)

def E_loc(conf,L):  #using skills to compute the ratio 
    box=[]
    for i in range(L):
        if conf[0][i]==1:
            if conf[0][left(i,L)]==0:
                box.append(Ratio(conf,i,left(i,L),L)[0])
            if conf[0][right(i,L)]==0:
                box.append(Ratio(conf,i,right(i,L),L)[0])
            
        if conf[0][i+L]==1:
            if conf[0][left(i,L)+L]==0:
                box.append(Ratio(conf,i+L,left(i,L)+L,L)[0])
            if conf[0][right(i,L)+L]==0:
                box.append(Ratio(conf,i+L,right(i,L)+L,L)[0])
    return -sum(box)

def E_loc4(conf,L,N_up):
    box=[]
    for i in range(L):
        if conf[0][i]==1:
            if conf[0][left(i,L)]==0:
                box.append(Ratio4(conf,i,left(i,L),L))
            if conf[0][right(i,L)]==0:
                box.append(Ratio4(conf,i,right(i,L),L))
            
        if conf[0][i+L]==1:
            if conf[0][left(i,L)+L]==0:
                box.append(Ratio(conf,i+L,left(i,L)+L,L)[0])
            if conf[0][right(i,L)+L]==0:
                box.append(Ratio(conf,i+L,right(i,L)+L,L)[0])
    return -sum(box)
    


if __name__=='__main__' : 
    L=2
    N_up=1
    conf=conf_initial(L,N_up)
    bb=E_loc(conf,L)
    bb1=E_loc1(conf,L)