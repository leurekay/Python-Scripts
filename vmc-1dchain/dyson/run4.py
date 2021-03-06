# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 19:52:54 2016

Based on run4!

a certain number of configurations was discarded,
at the beginning of Markov chain.
Beacause 此时的构型还没有收敛到平衡分布
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

L=24
N_up=12
steps=3000
sample_goal=L*steps

def hop(conf,L,u):
    s=random.randrange(0,L) #select in L
    num=-1
    for i in range(2*L):
        if conf[0][i]==1:
            num=num+1
        if num==s:
            break
    select=i    #map select to 2*L**2
    if select<L:
        flag=0   #spin up
    else:
        flag=1  #spin down

    left_index=left(select-flag*L,L)+flag*L       
    right_index=right(select-flag*L,L)+flag*L
    neighbour=[left_index,right_index]        
    hop_index=random.choice(neighbour)
    if conf[0][hop_index]==1:
        return "reject"
            
    #ratio=Ratio(conf,select,hop_index,L,u)[0] #skill
    ratio=Ratio1(conf,select,hop_index,L,u) #brute
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
h,dia,u=H(L)
while True:
    samples=samples+1
    try_hop=hop(conf,L,u)
    if try_hop !="reject":        
        conf,ratio=try_hop
        #Eloc=E_loc(conf,L,u)   #skill
        Eloc=E_loc1(conf,L,u)  #brute
    
    if samples>sample_goal/4:
        E_total=E_total+Eloc
        if samples==sample_goal:
            break
E=E_total/(samples*0.75)
E_site=E/L

run_time=time.time()-start_time 
print "run time:%d seconds"%run_time 

f = open('C:/Users/aa/Documents/Python Scripts/vmc-1dchain/rewrite/log4.txt', 'a+')
now=time.strftime("%Y-%m-%d %H:%M:%S")
f.write("E=%.4f E_site=%4f steps=%d  L=%d  N_up=%d  run_time=%.1fs  "%(E,E_site,steps,L,N_up,run_time)+"\n\n")
f.close()

