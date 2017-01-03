# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 17:41:39 2016
基于run11的遍历。固定J
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

L=2
j=3
mc=0.15
md=0.05
v=1.4
Nwarmup=15000
Nstep=15000
#sample_goal=steps*L**2





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
        ratio1=Ratio1(conf,s_conf_index,opposite_spin,L,j,mc,md,v,u)
        ratio2=Ratio1(conf_temp,opposite_ele,same_ele,L,j,mc,md,v,u)
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

def warm_up(Nwarmup,conf,L,mc,md,v,u):
    while Nwarmup:
        Nwarmup=Nwarmup-1
        for i in range(3*L**2):
            try_hop=ele_hop(conf,L,mc,md,v,u)
            if try_hop != "reject":
                ratio,conf=try_hop
        for i in range(2*L**2):
            try_spin=spin_flip(conf,L,mc,md,v,u)
            if try_spin != "reject":
                ratio,conf=try_spin
    return conf

def measure(L,j,mc,md,v): 
    
    start_time=time.time()

    box=[]
    samples=0
    sample_hop=0
    sample_spin=0  
    E_total1=0 
    E_total2=0 
    E_total3=0
    p1=Hamiltonian(L,j,mc,md,v)
    u=p1.unitary
    dia=p1.diagonal
    conf_new=conf_initial(L)
    conf_new=warm_up(Nwarmup,conf_new,L,mc,md,v,u)
    E_loc1=E_parra_loc(conf_new,L,j)
    E_loc2=E_loc_hop(conf_new,L,j,mc,md,v,u)
    E_loc3=E_loc_spin1(conf_new,L,j,mc,md,v,u)
    
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
    Esquare_total=0
    
    conf_new=warm_up(Nwarmup,conf_new,L,mc,md,v,u)
    while True:
        for i in range(3*L**2):
            try_hop=ele_hop(conf_new,L,mc,md,v,u)
            if try_hop != "reject":
                ratio,conf_new=try_hop
        for i in range(2*L**2):
            try_spin=spin_flip(conf_new,L,mc,md,v,u)
            if try_spin != "reject":
                ratio,conf_new=try_spin
        if samples%(1)==0:    
            E_loc1=E_parra_loc(conf_new,L,j)
            E_loc2=E_loc_hop(conf_new,L,j,mc,md,v,u)
            E_loc3=E_loc_spin1(conf_new,L,j,mc,md,v,u)
            E_loc=E_loc1+E_loc2+E_loc3
            Esquare_total=Esquare_total+E_loc**2
            ordermcA_loc=orderMcA(conf_new,L)
            ordermcB_loc=orderMcB(conf_new,L)
            ordermdA_loc=orderMdA(conf_new,L)
            ordermdB_loc=orderMdB(conf_new,L)
            orderV_loc=orderV(conf_new,L,j,mc,md,v,u)
            orderV1_loc=orderV1(conf_new,L,j,mc,md,v,u)
            E_total1=E_total1+E_loc1
            E_total2=E_total2+E_loc2
            E_total3=E_total3+E_loc3
            mcA_total=mcA_total+ordermcA_loc
            mcB_total=mcB_total+ordermcB_loc
            mdA_total=mdA_total+ordermdA_loc
            mdB_total=mdB_total+ordermdB_loc
            V_total=V_total+orderV_loc
            V1_total=V1_total+orderV1_loc       
        samples=samples+1     
        if samples==Nstep:
            break
            
    E1=E_total1/Nstep
    E2=E_total2/Nstep
    E3=E_total3/Nstep
    E=E1+E2+E3
    Esquare=Esquare_total/Nstep
    variance=(Esquare-E**2)/(4*L**2)
    E_cell1=E1/L**2
    E_cell2=E2/L**2
    E_cell3=E3/L**2
    E_cell=E_cell1+E_cell2+E_cell3
    E_ele=E_cell/4
    OmcA=mcA_total/Nstep
    OmcB=mcB_total/Nstep
    OmdA=mdA_total/Nstep
    OmdB=mdB_total/Nstep
    Ov=V_total/Nstep
    Ov1=V1_total/Nstep
    
    run_time=time.time()-start_time 
    print "run time:%d seconds"%run_time   
    
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    f = open('C:/Users/aa/Documents/Python Scripts/vmc-klm5/j='+str(j)+'a.txt', 'a+')
    f.write("E_cell1=%.3f E_cell2=%.3f E_cell3=%.3f E_cell=%.3f Nstep=%d  L=%d  j=%.2f  mc=%.2f  md=%.2f  v=%.2f  run_time=%.1fs  "%(E_cell1,E_cell2,E_cell3,E_cell,Nstep,L,j,mc,md,v,run_time)+now+"\n\n")
    f.close()
    return [E_ele,variance,(OmcA+OmcB)/2,(OmdA+OmdB)/2,(Ov+Ov1)/2]

mc_range=np.arange(0.05,0.4,0.05)
md_range=np.arange(0.05,0.4,0.05)
v_range=np.arange(0.6,1.6,0.1)
f = open('C:/Users/aa/Documents/Python Scripts/vmc-klm5/j='+str(j)+'.txt', 'a+')
f.write("-----------------------------------------------------------------------\n")
f.write("-----------------------------------------------------------------------\n")
f.write("-----------------------------------------------------------------------\n")
f.write("L=%d    j=%.2f    Nwarmup=%d    Nstep=%d"%(L,j,Nwarmup,Nstep)+"\n\n")
f.write("-----------------------------------------------------------------------\n")
f.close()
for mc in mc_range:
    for md in md_range:
        for v in v_range:
            E_ele,variance,Omc,Omd,Ov=measure(L,j,mc,md,v)
            f = open('C:/Users/aa/Documents/Python Scripts/vmc-klm5/j='+str(j)+'.txt', 'a+')
            f.write("E_ele=%.3f Var=%.3f Omc=%.3f Omd=%.3f Ov=%.3f  (%.2f,%.2f,%.2f)"%(E_ele,variance,Omc,Omd,Ov,mc,md,v)+"\n\n")
            f.close()
