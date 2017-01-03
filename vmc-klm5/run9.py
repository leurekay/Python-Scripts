# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 18:33:22 2016
在run8的基础上，增加了计算序参量的功能
@author: aa
"""


from __future__ import division
import random,copy,time
import numpy as np
from bound import *
from configure import conf_initial
from mfh import Hamiltonian
from slater import *
from observable import *
start_time=time.time()
L=4
j=0.9
mc=0.6
md=0.3
v=0.3
steps=10000
sample_goal=steps*L**2
conf_new=conf_initial(L)


conf_total=[conf_new.copy()]
print conf_new




def ele_hop(conf_new,L,mc,md,v,u):
    while True:
        s_ele_index=random.randrange(0,4*L**2)  #index of ele in 4*L**2
        cell=s_ele_index//4   #index of cell
        s_conf_index=cell*8+s_ele_index%4
        if conf_new[0][s_conf_index]==1:
            break
    A_B=(s_ele_index%4)%2       #0:A   1:B
    Up_Down=(s_ele_index%4)//2   #0:up  1:down      
    neigh_cell_index=[middle(cell,L),(1-A_B)*left(cell,L)+A_B*right(cell,L),(1-A_B)*down(cell,L)+A_B*up(cell,L)]
    hop_cell_index=random.choice(neigh_cell_index) 
    hop_conf_index=hop_cell_index*8+2*Up_Down+1-A_B
    if conf_new[0][hop_conf_index] == 1:
        return "reject" 
    
    #print hop_conf_index
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
        s=random.randrange(0,4*L*L)
        cell=s//4
        s_conf_index=cell*8+4+s%4     #map to total conf
        opposite_spin=cell*8+4+(s%4+2)%4
        same_ele=cell*8+s%4
        opposite_ele=cell*8+(s%4+2)%4
        if conf[0][s_conf_index]==2:
            break
    if conf[0][same_ele]==0 and conf[0][opposite_ele] !=0:
        conf_temp=conf.copy()
        conf_temp[0][s_conf_index]=0
        conf_temp[0][opposite_spin]=2
        ratio1=Ratio(conf,s_conf_index,opposite_spin,L,j,mc,md,v,u)
        ratio2=Ratio(conf_temp,opposite_ele,same_ele,L,j,mc,md,v,u)
        ratio=ratio1*ratio2
        rho=ratio.conjugate()*ratio
        if random.uniform(0,1)<min(1,rho):
            conf_temp[0][opposite_ele]=0
            conf_temp[0][same_ele]=1 
            return ratio,conf_temp
        else:
            return "reject"  
    else:
        return "reject"
    

def spin_flip1(conf,L,mc,md,v,u):
    flag=0      #invoid of die loop
    while True:
        flag=flag+1
        if flag==100:
            #pass
            return "reject"
        s=random.randrange(0,4*L*L)
        cell=s//4
        s_conf_index=cell*8+4+s%4     #map to total conf
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
            rho=ratio.conjugate()*ratio
            if random.uniform(0,1)<min(1,rho):
                conf_temp[0][opposite_ele]=0
                conf_temp[0][same_ele]=1 
                return ratio,conf_temp
            else:
                return "reject"            



box=[]
samples=0
den=0
sample_hop=0
sample_spin=0  
E_total=0 
p1=Hamiltonian(L,j,mc,md,v)
u=p1.unitary
u=u.real
dia=p1.diagonal
E_loc=E_parra_loc(conf_new,L,j)+E_loc_hop(conf_new,L,j,mc,md,v,u)+E_loc_spin(conf_new,L,j,mc,md,v,u)

ordermcA_loc=orderMcA(conf_new,L)
ordermcB_loc=orderMcB(conf_new,L)
ordermdA_loc=orderMdA(conf_new,L)
ordermdB_loc=orderMdB(conf_new,L)
orderV_loc=orderV(conf_new,L,j,mc,md,v,u)
orderV1_loc=orderV1(conf_new,L,j,mc,md,v,u)
mcA_total=0
mcB_total=0 
mdA_total=0
mdB_total=0
V_total=0
V1_total=0
while True:    
    try_hop=ele_hop(conf_new,L,mc,md,v,u)
    if try_hop != "reject":
        ratio,conf_new=try_hop
        conf_total.append(conf_new.copy())
        sample_hop=sample_hop+1
        if samples>sample_goal//2:
            E_loc=E_parra_loc(conf_new,L,j)+E_loc_hop(conf_new,L,j,mc,md,v,u)+E_loc_spin(conf_new,L,j,mc,md,v,u)
            ordermcA_loc=orderMcA(conf_new,L)
            ordermcB_loc=orderMcB(conf_new,L)
            ordermdA_loc=orderMdA(conf_new,L)
            ordermdB_loc=orderMdB(conf_new,L)
            orderV_loc=orderV(conf_new,L,j,mc,md,v,u)
            orderV1_loc=orderV1(conf_new,L,j,mc,md,v,u)

    if samples>sample_goal//2 and samples%(L**2)==0:
        E_total=E_total+E_loc
        mcA_total=mcA_total+ordermcA_loc
        mcB_total=mcB_total+ordermcB_loc
        mdA_total=mdA_total+ordermdA_loc
        mdB_total=mdB_total+ordermdB_loc
        V_total=V_total+orderV_loc
        V1_total=V1_total+orderV1_loc
        box.append(E_loc)
        den=den+1
    samples=samples+1
    if samples==sample_goal:
        break
  
  
    try_spin=spin_flip(conf_new,L,mc,md,v,u)
    if try_spin != "reject":
        ratio,conf_new=try_spin
        conf_total.append(conf_new.copy())
        sample_spin=sample_spin+1
        if samples>sample_goal//2 :
            E_loc=E_parra_loc(conf_new,L,j)+E_loc_hop(conf_new,L,j,mc,md,v,u)+E_loc_spin(conf_new,L,j,mc,md,v,u)
            ordermcA_loc=orderMcA(conf_new,L)
            ordermcB_loc=orderMcB(conf_new,L)
            ordermdA_loc=orderMdA(conf_new,L)
            ordermdB_loc=orderMdB(conf_new,L)
            orderV_loc=orderV(conf_new,L,j,mc,md,v,u)
            orderV1_loc=orderV1(conf_new,L,j,mc,md,v,u)
    if samples>sample_goal//2 and samples%(L**2)==0:   
        E_total=E_total+E_loc
        mcA_total=mcA_total+ordermcA_loc
        mcB_total=mcB_total+ordermcB_loc
        mdA_total=mdA_total+ordermdA_loc
        mdB_total=mdB_total+ordermdB_loc
        V_total=V_total+orderV_loc
        V1_total=V1_total+orderV1_loc
        box.append(E_loc)
        den=den+1
    samples=samples+1
    if samples==sample_goal:
        break
E=E_total/den
E_cell=E/L**2
OmcA=mcA_total/den
OmcB=mcB_total/den
OmdA=mdA_total/den
OmdB=mdB_total/den
Ov=V_total/den
Ov1=V1_total/den

run_time=time.time()-start_time 
print "run time:%d seconds"%run_time   

f = open('C:/Users/aa/Documents/Python Scripts/vmc-klm5/log9.txt', 'a+')
now=time.strftime("%Y-%m-%d %H:%M:%S")
f.write("E=%.3f  E_cell=%.3f  steps=%d  L=%d  j=%.2f  mc=%.2f  md=%.2f  v=%.2f  run_time=%.1fs  "%(E,E_cell,steps,L,j,mc,md,v,run_time)+now+"\n\n")
f.close()
