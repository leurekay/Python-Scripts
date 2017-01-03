# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 11:45:08 2016

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
L=2
j=1.7
mc=0.2
md=0.3
v=0.8
Nwarmup=10000
Nstep=5000
LOOP=1              #for LOOP monte-carlo-step,do measure
path='C:/Users/aa/Documents/Python Scripts/vmc-klm5/log13.txt'
testGG=0  #test
def ele_hop(G,Gindex,conf_new,L,mc,md,v,u):
    global testGG #test
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
    before=s_conf_index
    after=hop_conf_index
    u=u.T
    beta=Gindex.index(before)     
    M=u[np.arange(0,L*L*4,1),:]
    u=u.T
    SIGMA=M[:,before]-M[:,after]
    ratio=1-np.dot(G[beta,:],SIGMA)   
    #test
    #u=u.T          
    #test
    Ginv=M[:,Gindex]  
    #test
    ratio1=Ratio(conf_new,s_conf_index,hop_conf_index,L,j,mc,md,v,u)
    rho=ratio.conjugate()*ratio
    print conf_new   #test
    print before,after  #test
    print ratio, ratio1  #test
    testGG=G*Ginv   #test
    if random.uniform(0,1)<min(1,rho):
        print "updated" #test0
        conf_new[0][s_conf_index]=0
        conf_new[0][hop_conf_index]=1 
        G_new=G+(np.dot(np.dot(G,SIGMA),G[beta,:]))/ratio
        Gindex_new=copy.copy(Gindex)    
        Gindex_new[beta]=after  
        return ratio,conf_new,G_new,Gindex_new
    else:
        return "reject"

def spin_flip1(conf,L,mc,md,v,u):   
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
def spin_flip(conf,L,mc,md,v,u):
    cell=random.randrange(0,L*L)
    A_B=random.choice([0,1])
    ele_up=cell*8+0+A_B
    ele_down=cell*8+2+A_B
    spin_up=cell*8+4+A_B
    spin_down=cell*8+6+A_B
    #ratio=Ratio_exchange1(conf,cell,A_B,L,j,mc,md,v,u)
    ratio=Ratio_exchange(conf,cell,A_B,L,j,mc,md,v,u)
    if ratio != "invalid" :
        if conf[0][spin_up]==2 and conf[0][ele_up]==0 and conf[0][ele_down]==1:
            conf_temp=np.copy(conf)
            conf_temp[0][ele_up]=1
            conf_temp[0][ele_down]=0
            conf_temp[0][spin_up]=0
            conf_temp[0][spin_down]=2
        else:
            conf_temp=np.copy(conf)
            conf_temp[0][ele_up]=0
            conf_temp[0][ele_down]=1
            conf_temp[0][spin_up]=2
            conf_temp[0][spin_down]=0
        rho=ratio.conjugate()*ratio
        rho=rho.real
        if random.uniform(0,1)<min(1,rho):
            return ratio,conf_temp
        else:
            return "reject" 
    else:
        return "reject"
        


conf_new=conf_initial(L)

box=[]
samples=0
den=0
sample_hop=0
sample_spin=0  
E_total1=0 
E_total2=0 
E_total3=0
p1=Hamiltonian(L,j,mc,md,v)
u=p1.unitary
M=u[:,np.arange(0,L*L*4,1)]
#u=u.real
dia=p1.diagonal
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
Esquare_total1=0
Esquare_total2=0
Esquare_total3=0

count=0
percent=0
kedu=Nwarmup/100

G,Gindex=G_and_Idx(conf_new,L,j,mc,md,v,u)
while Nwarmup:
    count=count+1
    Nwarmup=Nwarmup-1
    G,Gindex=G_and_Idx(conf_new,L,j,mc,md,v,u)
    for i in range(3*L**2):
        try_hop=ele_hop(G,Gindex,conf_new,L,mc,md,v,u)
        if try_hop != "reject":
            ratio,conf_new,G,Gindex=try_hop
    for i in range(2*L**2):
        try_spin=spin_flip(conf_new,L,mc,md,v,u)
        if try_spin != "reject":
            ratio,conf_new=try_spin
    if count %kedu ==0:
        print "warm-up:%d"%percent+"%"
        percent=percent+1
        count=0

while True: 
    loop=LOOP
    while loop:
        loop=loop-1   
        G,Gindex=G_and_Idx(conf_new,L,j,mc,md,v,u)
        for i in range(3*L**2):
            try_hop=ele_hop(G,Gindex,conf_new,L,mc,md,v,u)
            if try_hop != "reject":
                ratio,conf_new,G,Gindex=try_hop
                sample_hop=sample_hop+1
        for i in range(2*L**2):
            try_spin=spin_flip(conf_new,L,mc,md,v,u)
            if try_spin != "reject":
                ratio,conf_new=try_spin   
                sample_spin=sample_spin+1
    if samples%(1)==0:
        
        E_loc1=E_parra_loc(conf_new,L,j)
        E_loc2=E_loc_hop1(conf_new,L,j,mc,md,v,u)
        #E_loc3=E_loc_spin1(conf_new,L,j,mc,md,v,u)
        #E_loc3=E_loc_spin3(conf_new,L,j,mc,md,v,u)
        E_loc3=E_loc_spin5(conf_new,L,j,mc,md,v,u)
        E_loc=E_loc1+E_loc2+E_loc3
        if abs(E_loc)>1000:
            print E_loc
            print conf_new
        Esquare_total=Esquare_total+E_loc**2
        Esquare_total1=Esquare_total1+E_loc1**2
        Esquare_total2=Esquare_total2+E_loc2**2
        Esquare_total3=Esquare_total3+E_loc3**2
        
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
    
accHop=sample_hop/(LOOP*Nstep*3*L**2)   
accSpin=sample_spin/(LOOP*Nstep*2*L**2)
acc=(sample_hop+sample_spin)/(LOOP*Nstep*5*L**2)
  
E1=E_total1/Nstep
E2=E_total2/Nstep
E3=E_total3/Nstep
E=E1+E2+E3
Esquare=Esquare_total/Nstep
Esquare1=Esquare_total1/Nstep
Esquare2=Esquare_total2/Nstep
Esquare3=Esquare_total3/Nstep

variance=(Esquare-E**2)/(Nstep-1)/(4*L**2)
variance1=(Esquare1-E1**2)/(Nstep-1)/(4*L**2)
variance2=(Esquare2-E2**2)/(Nstep-1)/(4*L**2)
variance3=(Esquare3-E3**2)/(Nstep-1)/(4*L**2)

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

f = open(path, 'a+')
now=time.strftime("%Y-%m-%d %H:%M:%S")
f.write("L=%d j=%.2f (%.2f,%.2f,%.2f) {%d,%d} LOOP=%d acc=(%.2f,%.2f,%.2f) run_time=%.1fs  "%(L,j,mc,md,v,Nwarmup,Nstep,LOOP,acc,accHop,accSpin,run_time)+now+"\n\n")
f.write("e=%.4f var=%.2e [%.3f_%.3f %.3f_%.3f %.3f_%.3f] (%.4f %.4f %.4f ) (%.2e %.2e %.2e )"%(E_ele,variance,OmcA,OmcB,OmdA,OmdB,Ov,Ov1,E_cell1,E_cell2,E_cell3,variance1,variance2,variance3)+"\n\n")
f.close()

