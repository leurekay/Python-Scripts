# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:57:25 2016
即使hopping被拒绝了，也计次
@author: aa
"""
from __future__ import division
from math import *
import numpy as np
import random,time
from hamiltonian import *
from configuration import conf_initial
from slater import *
from observable import *
start_time=time.time()

L=30
N_up=15
steps=1000
sample_goal=L*steps

def hop(conf,L):
    while True:
        s=random.randrange(0,L) #select in L**2
        num=-1
        for i in range(2*L):
            if conf[0][i]==1:
                num=num+1
            if num==s:
                break
        select=i    #map select to 2*L**2
        if select<L:
            flag=0
        else:
            flag=1
        neighbour=[]

        left_index=left(select-flag*L,L)+flag*L       
        right_index=right(select-flag*L,L)+flag*L
       
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
conf=conf_initial(L,N_up)
samples=0

E_total=0
while True:
    samples=samples+1
    try_hop=hop(conf,L)
    if try_hop !="reject":        
        conf,ratio=try_hop
        Eloc=E_loc1(conf,L)
    
    E_total=E_total+Eloc
    if samples==sample_goal:
        break
E=E_total/samples
E_site=E/L

run_time=time.time()-start_time 
print "run time:%d seconds"%run_time 

f = open('C:/Users/aa/Documents/Python Scripts/vmc-1dchain/log2.txt', 'a+')
now=time.strftime("%Y-%m-%d %H:%M:%S")
f.write("E=%.4f E_site=%4f steps=%d  L=%d  N_up=%d  run_time=%.1fs  "%(E,E_site,steps,L,N_up,run_time)+"\n\n")
f.close()
