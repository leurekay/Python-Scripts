# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:14:48 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import random
from hamiltonian import *
from configuration import conf_initial
from slater import Ratio
sample_goal=4000
L=12

def hop(conf,L):
    while True:
        s=random.randrange(0,L*L) #select in L**2
        num=-1
        for i in range(2*L*L):
            if conf[0][i]==1:
                num=num+1
            if num==s:
                break
        select=i    #map select to 2*L**2
        if select<L*L:
            flag=0
        else:
            flag=1
        neighbour=[]
        up_index=up(select-flag*L*L,L)+flag*L*L
        down_index=down(select-flag*L*L,L)+flag*L*L
        left_index=left(select-flag*L*L,L)+flag*L*L        
        right_index=right(select-flag*L*L,L)+flag*L*L
        if conf[0][up_index]==0:
            neighbour.append(up_index)
        if conf[0][down_index]==0:
            neighbour.append(down_index)
        if conf[0][left_index]==0:
            neighbour.append(left_index)
        if conf[0][right_index]==0:
            neighbour.append(right_index)
        if len(neighbour)==0:
            continue
        else:
            hop_index=random.choice(neighbour)
            break

    ratio=Ratio(conf,select,hop_index,L)[0]
    rho=(ratio*ratio.conjugate()).real
    print rho
    if random.uniform(0,1)<min(1,rho):
        conf[0][select]=0
        conf[0][hop_index]=1 
        return [conf,ratio]
    else:
        return "reject"
conf=conf_initial(L)
samples=0
E_total=0
while True:
    try_hop=hop(conf,L)
    if try_hop !="reject":
        
        samples=samples+1
        conf,ratio=try_hop
        E_total=E_total-ratio-1/ratio
    if samples==sample_goal:
        break
E=E_total/sample_goal
E_site=E_total/sample_goal/L**2    
    