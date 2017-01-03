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

def E_loc3(conf,L,u,N_up):
    box=[]
    for i in range(L):
        if conf[0][i]==1:
            if conf[0][left(i,L)]==0:
                box.append(Ratio3(conf,i,left(i,L),L,N_up))
            if conf[0][right(i,L)]==0:
                box.append(Ratio3(conf,i,right(i,L),L,N_up))
            
        if conf[0][i+L]==1:
            if conf[0][left(i,L)+L]==0:
                box.append(Ratio3(conf,i+L,left(i,L)+L,L,N_up))
            if conf[0][right(i,L)+L]==0:
                box.append(Ratio3(conf,i+L,right(i,L)+L,L,N_up))
    return -sum(box).real


def E_loc4(conf,L,u,N_up):
    box=[]
    for i in range(L):
        if conf[0][i]==1:
            if conf[0][left(i,L)]==0:
                box.append(Ratio4(conf,i,left(i,L),L,N_up))
            if conf[0][right(i,L)]==0:
                box.append(Ratio4(conf,i,right(i,L),L,N_up))
            
        if conf[0][i+L]==1:
            if conf[0][left(i,L)+L]==0:
                box.append(Ratio4(conf,i+L,left(i,L)+L,L,N_up))
            if conf[0][right(i,L)+L]==0:
                box.append(Ratio4(conf,i+L,right(i,L)+L,L,N_up))
    return -sum(box).real


if __name__=='__main__' : 
    L=36
    N_up=18
    h,dia,u=H(L)

    conf=conf_initial(L,N_up)
    b0=E_loc(conf,L,u)
    b1=E_loc1(conf,L,u)
    b3=E_loc3(conf,L,u,N_up)
    b4=E_loc4(conf,L,u,N_up)