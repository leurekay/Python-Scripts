# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:52:50 2016
根据已知的波函数，求可观测量的值。主要是求能量
10月18日下午，宿管敲门之际，发现一重大BUG：E_parra_loc中
把正负号弄反了

10月22晚，E_loc_spin和E_loc_spin1的区别是调用的Ratio不同
10月23晚，发现计算序参量V时，忘记除2*L**2

E_loc_hop：调用技巧的ratio
E_loc_hop1:调用蛮力ratio1
E_loc_spin:巡游电子，局域电子，分别hop到相反自旋的位置
           调用技巧ratio
E_loc_spin1:调用蛮力ratio1
E_loc_spin2:
@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import random,time,copy
from mfh import *
from bound import *
from slater import *
from configure import conf_initial


def E_loc_hop(conf,L,j,mc,md,v,u):  #using skills to compute the ratio 
    box=[]
    for s_ele_index in range(4*L**2):
        cell=s_ele_index//4   
        s_conf_index=cell*8+s_ele_index%4
        A_B=(s_ele_index%4)%2       #0:A   1:B
        Up_Down=(s_ele_index%4)//2   #0:up  1:down 
        if conf[0][s_conf_index]==1:
            neigh_cell_index=[middle(cell,L),(1-A_B)*left(cell,L)+A_B*right(cell,L),(1-A_B)*down(cell,L)+A_B*up(cell,L)]
            for i in neigh_cell_index:
                ii=i*8+2*Up_Down+1-A_B
                if conf[0][ii]==0:
                    #print ii
                    box.append(Ratio(conf,s_conf_index,ii,L,j,mc,md,v,u))
    return -sum(box)

def E_loc_spin(conf,L,j,mc,md,v,u):
    box=[]
    for s in range(4*L**2):
        cell=s//4
        s_conf_index=cell*8+4+s%4     
        opposite_spin=cell*8+4+(s%4+2)%4
        same_ele=cell*8+s%4
        opposite_ele=cell*8+(s%4+2)%4
        if conf[0][s_conf_index] !=0  and conf[0][same_ele]==0 and conf[0][opposite_ele] !=0:
            conf_temp=conf.copy()
            conf_temp[0][s_conf_index]=0
            conf_temp[0][opposite_spin]=2
            ratio1=Ratio(conf,s_conf_index,opposite_spin,L,j,mc,md,v,u)
            ratio2=Ratio(conf_temp,opposite_ele,same_ele,L,j,mc,md,v,u)
            ratio=ratio1*ratio2
            box.append(ratio)
    return 0.5*j*sum(box)

def E_loc_hop1(conf,L,j,mc,md,v,u):  
    box=[]
    for s_ele_index in range(4*L**2):
        cell=s_ele_index//4   
        s_conf_index=cell*8+s_ele_index%4
        A_B=(s_ele_index%4)%2       #0:A   1:B
        Up_Down=(s_ele_index%4)//2   #0:up  1:down 
        if conf[0][s_conf_index]==1:
            neigh_cell_index=[middle(cell,L),(1-A_B)*left(cell,L)+A_B*right(cell,L),(1-A_B)*down(cell,L)+A_B*up(cell,L)]
            for i in neigh_cell_index:
                ii=i*8+2*Up_Down+1-A_B
                if conf[0][ii]==0:
                    #print ii
                    box.append(Ratio1(conf,s_conf_index,ii,L,j,mc,md,v,u))
    return -sum(box)
    


def E_loc_spin1(conf,L,j,mc,md,v,u):
    box=[]
    for s in range(4*L**2):
        cell=s//4
        s_conf_index=cell*8+4+s%4     
        opposite_spin=cell*8+4+(s%4+2)%4
        same_ele=cell*8+s%4
        opposite_ele=cell*8+(s%4+2)%4
        if conf[0][s_conf_index] !=0  and conf[0][same_ele]==0 and conf[0][opposite_ele] !=0:
            conf_temp=conf.copy()
            conf_temp[0][s_conf_index]=0
            conf_temp[0][opposite_spin]=2
            ratio1=Ratio1(conf,s_conf_index,opposite_spin,L,j,mc,md,v,u)
            ratio2=Ratio1(conf_temp,opposite_ele,same_ele,L,j,mc,md,v,u)
            ratio=ratio1*ratio2
            box.append(ratio)
    return 0.5*j*sum(box)
def E_parra_loc(conf,L,j):     
    total=0
    for i in range(L**2):        #iteration the cells
        total=total+conf[0][i*8+0]*conf[0][i*8+4]+conf[0][i*8+1]*conf[0][i*8+5]\
                   +conf[0][i*8+2]*conf[0][i*8+6]+conf[0][i*8+3]*conf[0][i*8+7]\
                   -conf[0][i*8+0]*conf[0][i*8+6]-conf[0][i*8+1]*conf[0][i*8+7]\
                   -conf[0][i*8+2]*conf[0][i*8+4]-conf[0][i*8+3]*conf[0][i*8+5]
    return total*j/8      #because each spin label "2",so need to divide 2   

def orderMcA(conf,L):
    box=[]
    for i in range(L**2):
        box.append(conf[0][i*8]-conf[0][i*8+2])
    return -0.5*sum(box)/L**2
def orderMcB(conf,L):
    box=[]
    for i in range(L**2):
        box.append(conf[0][i*8+1]-conf[0][i*8+3])
    return 0.5*sum(box)/L**2


def orderMdA(conf,L):
    box=[]
    for i in range(L**2):
        box.append(conf[0][i*8+4]-conf[0][i*8+6])
    return 0.5*sum(box)/L**2/2
def orderMdB(conf,L):
    box=[]
    for i in range(L**2):
        box.append(conf[0][i*8+5]-conf[0][i*8+7])
    return -0.5*sum(box)/L**2/2


def orderV(conf,L,j,mc,md,v,u):
    box=[]
    for i in range(L**2):
        if conf[0][i*8]==1 and conf[0][i*8+4]==0:
            box.append(Ratio(conf,i*8,i*8+4,L,j,mc,md,v,u))
        if conf[0][i*8+1]==1 and conf[0][i*8+5]==0:
            box.append(Ratio(conf,i*8+1,i*8+5,L,j,mc,md,v,u))
        if conf[0][i*8+6]==2 and conf[0][i*8+2]==0:
            box.append(Ratio(conf,i*8+6,i*8+2,L,j,mc,md,v,u))  
        if conf[0][i*8+7]==2 and conf[0][i*8+3]==0:
            box.append(Ratio(conf,i*8+7,i*8+3,L,j,mc,md,v,u))  
    return -sum(box)/(2*L**2)
    
def orderV1(conf,L,j,mc,md,v,u):
    box=[]
    for i in range(L**2):
        if conf[0][i*8+4]==2 and conf[0][i*8]==0:
            box.append(Ratio(conf,i*8+4,i*8,L,j,mc,md,v,u))
        if conf[0][i*8+5]==2 and conf[0][i*8+1]==0:
            box.append(Ratio(conf,i*8+5,i*8+1,L,j,mc,md,v,u))
        if conf[0][i*8+2]==1 and conf[0][i*8+6]==0:
            box.append(Ratio(conf,i*8+2,i*8+6,L,j,mc,md,v,u))  
        if conf[0][i*8+3]==1 and conf[0][i*8+7]==0:
            box.append(Ratio(conf,i*8+3,i*8+7,L,j,mc,md,v,u))  
    return -sum(box)/(2*L**2)

def E_loc_spin3(conf,L,j,mc,md,v,u):
    box=[]
    for cell in range(L**2):
        for A_B in [0,1]:
            ratio=Ratio_exchange(conf,cell,A_B,L,j,mc,md,v,u)
            if ratio !="invalid" :
                box.append(ratio)
    return -0.5*j*sum(box)

def E_loc_spin4(conf,L,j,mc,md,v,u):
    box=[]
    for cell in range(L**2):
        for A_B in [0,1]:
            ratio=Ratio_exchange1(conf,cell,A_B,L,j,mc,md,v,u)
            if ratio !="invalid" :
                box.append(ratio)
    return 0.5*j*sum(box)

def E_loc_spin5(conf,L,j,mc,md,v,u):
    box=[]
    for cell in range(L**2):
        for A_B in [0,1]:
            ratio=Ratio_exchange2(conf,cell,A_B,L,j,mc,md,v,u)
            if ratio !="invalid" :
                box.append(ratio)
    return -0.5*j*sum(box)

if __name__=='__main__' : 
    L=2
    j=3
    mc=0.01
    md=0.07
    v=1.15
    
    p1=Hamiltonian(L,j,mc,md,v)
    u=p1.unitary
    #u=u.real
    
    conf=conf_initial(L)
    conf=np.array([[1, 1, 1, 0, 0, 0, 2, 2, 1, 0, 0, 0, 2, 0, 0, 2, 0, 1, 1, 0, 0, 2, 2, 0, 1, 0, 0, 1, 2, 0, 0, 2]])
    b1=E_loc_hop(conf,L,j,mc,md,v,u)
    b2=E_loc_hop1(conf,L,j,mc,md,v,u) 
    
    c1=E_loc_spin(conf,L,j,mc,md,v,u)  
    c2=E_loc_spin1(conf,L,j,mc,md,v,u)
    c3=E_loc_spin3(conf,L,j,mc,md,v,u)
    c4=E_loc_spin4(conf,L,j,mc,md,v,u)
    c5=E_loc_spin5(conf,L,j,mc,md,v,u)
    