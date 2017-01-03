# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:48:48 2016

@author: aa
"""

from __future__ import division
import random,copy
import numpy as np
from bound import *
from configure import conf_initial
from slater_ratio import *
steps=10000
sample_goal=100
L=6
j=0.5
mc=0.4
md=0.3
v=0.8
conf_new=conf_initial(L)
conf_total=[conf_new.copy()]
print conf_new
def ele_hop(conf_new,L,mc,md,v):
    while True:
        s=random.randrange(0,4*L*L) #random a electron in eclctron conf
        s_conf_index=(s//4)*8+s%4         #map to total conf
        cell=s//4                   #cell index
        if s%2==0:                  #A sublattice
            vicinity=[middle(cell,L),left(cell,L),down(cell,L)] #3 neighborhood of cell
            hop_cell=random.choice(vicinity)   #random hopping ,label by cell
            hop_conf_index=8*hop_cell+s%4+1      #index by total conf
        else:                       #B sublattice
            vicinity=[middle(cell,L),left(cell,L),down(cell,L)]
            hop_cell=random.choice(vicinity)
            hop_conf_index=8*hop_cell+s%4-1
        if conf_new[0][s_conf_index] !=0 and conf_new[0][hop_conf_index]==0:
            ratio=Ratio(conf_new,s_conf_index,hop_conf_index,L,j,mc,md,v)
            rho=ratio**2
            if random.uniform(0,1)<min(1,rho):
                conf_new[0][s_conf_index]=0
                conf_new[0][hop_conf_index]=1 
                return [conf_new,ratio]
            else:
                return "reject"

def spin_flip(conf,L,mc,md,v):
    while True:
        s=random.randrange(0,4*L*L) #random a site in 2*L*L sites
        cell=s//4
        s_conf_index=(s//4)*8+4+s%4     #map to total conf
        """
        slected local spin is       (s//4)*8+4+s%4
                                      v   v    v  
                                      v   v    v 
        the other local spin is     (s//4)*8+4+(s%4+2)%4
        
        same spin c electron is     (s//4)*8+s%4
                                      ^   ^    ^ 
                                      ^   ^    ^
        opposite spin c electron is (s//4)*8+(s%4+2)%4
        """
        if conf_new[0][s_conf_index] !=0 and conf_new[0][(s//4)*8+s%4]==0 and conf_new[0][(s//4)*8+(s%4+2)%4] !=0:
            conf_temp=conf_new.copy()
            conf_temp[0][(s//4)*8+4+s%4]=0
            conf_temp[0][(s//4)*8+4+(s%4+2)%4]=2
            ratio=Ratio(conf_new,(s//4)*8+4+s%4,(s//4)*8+4+(s%4+2)%4,L,j,mc,md,v)*Ratio(conf_temp,(s//4)*8+(s%4+2)%4,(s//4)*8+s%4,L,j,mc,md,v)
            rho=ratio**2
            if random.uniform(0,1)<min(1,rho):
                conf_temp[0][(s//4)*8+(s%4+2)%4]=0
                conf_temp[0][(s//4)*8+s%4]=1 
                return [conf_temp,ratio]
                #break
            else:
                return "reject"
                #break
                
def E_parra_local():
    
    pass
def E_hop_local():
    pass
def E_spin_local():
    pass
                
samples=1 
samples_hop=0
samples_spin=0      
while True:
    try_hop=ele_hop(conf_new,L,mc,md,v)
    if try_hop !="reject":
        conf_new,ratio=try_hop
        conf_total.append(conf_new.copy())
        samples=samples+1
        samples_hop=samples_hop+1
    if samples==sample_goal:
        break
    
    
    try_spin=spin_flip(conf_new,L,mc,md,v)
    if try_spin !="reject":
        conf_new,ratio=try_spin
        conf_total.append(conf_new.copy())
        samples=samples+1
        samples_spin=samples_spin+1
    if samples==sample_goal:
        break