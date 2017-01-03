# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:39:01 2016

@author: aa
"""
from __future__ import division
import random,copy,time
import numpy as np
from bound import *
from configure import conf_initial
from mfh import Hamiltonian
from slater import *
start_time=time.time()
L=6
j=1
mc=0.4
md=0.4
v=0.5
steps=500
sample_goal=steps*L**2
conf_new=conf_initial(L)


conf_total=[conf_new.copy()]
print conf_new




def ele_hop(conf_new,L,mc,md,v,u):
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
            ratio=Ratio(conf_new,s_conf_index,hop_conf_index,L,j,mc,md,v,u)
            rho=ratio.conjugate()*ratio
            if random.uniform(0,1)<min(1,rho):
                conf_new[0][s_conf_index]=0
                conf_new[0][hop_conf_index]=1 
                return ratio,conf_new
            else:
                return "reject"

def spin_flip(conf,L,mc,md,v,u):
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
            ratio1=Ratio(conf_new,(s//4)*8+4+s%4,(s//4)*8+4+(s%4+2)%4,L,j,mc,md,v,u)
            ratio2=Ratio(conf_temp,(s//4)*8+(s%4+2)%4,(s//4)*8+s%4,L,j,mc,md,v,u)
            ratio=ratio1*ratio2
            rho=ratio.conjugate()*ratio
            if random.uniform(0,1)<min(1,rho):
                conf_temp[0][(s//4)*8+(s%4+2)%4]=0
                conf_temp[0][(s//4)*8+s%4]=1 
                return ratio,conf_temp
                #break
            else:
                return "reject"

def E_parra_loc(conf,L,j):     
    total=0
    for i in range(L**2):        #iteration the cells
        total=total+conf[0][i*8+0]*conf[0][i*8+4]+conf[0][i*8+1]*conf[0][i*8+5]\
                   +conf[0][i*8+2]*conf[0][i*8+6]+conf[0][i*8+3]*conf[0][i*8+7]\
                   -conf[0][i*8+0]*conf[0][i*8+6]+conf[0][i*8+1]*conf[0][i*8+7]\
                   -conf[0][i*8+2]*conf[0][i*8+4]+conf[0][i*8+3]*conf[0][i*8+5]
    return total*j/8      #because each spin label "2",so need to divide 2   

samples=0
sample_hop=0
sample_spin=0  
E_total=0  
p1=Hamiltonian(L,j,mc,md,v)
u=p1.unitary
u=u.real
dia=p1.diagonal   
while True:
    
    try_hop=ele_hop(conf_new,L,mc,md,v,u)
    if try_hop != "reject":
        ratio,conf_new=try_hop
        conf_total.append(conf_new.copy())
        samples=samples+1
        sample_hop=sample_hop+1
        E_total=E_total+E_parra_loc(conf_new,L,j)-ratio
        E_total=E_total+E_parra_loc(conf_new,L,j)-ratio-1/ratio
        if samples==sample_goal:
            break
    try_spin=spin_flip(conf_new,L,mc,md,v,u)
    if try_spin != "reject":
        ratio,conf_new=try_spin
        conf_total.append(conf_new.copy())
        samples=samples+1
        sample_spin=sample_spin+1
        #E_total=E_total+E_parra_loc(conf_new,L,j)+0.5*j*ratio
        E_total=E_total+E_parra_loc(conf_new,L,j)+0.5*j*(ratio+1/ratio)
        if samples==sample_goal:
            break
E=E_total/samples
E_cell=E/L**2

run_time=time.time()-start_time 
print "run time:%d seconds"%run_time   

f = open('C:/Users/aa/Documents/Python Scripts/vmc-klm5/log.txt', 'a+')
now=time.strftime("%Y-%m-%d %H:%M:%S")
f.write("E=%.3f  steps=%d  L=%d  j=%.2f  mc=%.2f  md=%.2f  v=%.2f  run_time=%.1fs  "%(E,steps,L,j,mc,md,v,run_time)+now+"\n\n")
f.close()