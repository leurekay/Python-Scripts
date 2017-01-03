# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:01:42 2016
if a peoposed configuration was rejected,still save it in
conf set,
@author: aa
"""

from __future__ import division
import random,copy
import numpy as np
from bound import *
from configure import conf_initial
from slater_ratio import *
from local import *
steps=10000
sample_goal=15000
L=6
j=0.5
mc=-0.00423200583180579
md=-0.03802405130574126
v=-0.00211303733830379
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
            ratio,occupy_index,W,u,dia=Ratio(conf_new,s_conf_index,hop_conf_index,L,j,mc,md,v)
            rho=ratio**2
            if random.uniform(0,1)<min(1,rho):
                conf_new[0][s_conf_index]=0
                conf_new[0][hop_conf_index]=1 
                return [conf_new,ratio,occupy_index,W,u,dia]
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
            ratio1,occupy_index,W,u,dia=Ratio(conf_new,(s//4)*8+4+s%4,(s//4)*8+4+(s%4+2)%4,L,j,mc,md,v)
            ratio2,null,null,null,null=Ratio(conf_temp,(s//4)*8+(s%4+2)%4,(s//4)*8+s%4,L,j,mc,md,v)
            rho=(ratio1*ratio2)**2
            if random.uniform(0,1)<min(1,rho):
                conf_temp[0][(s//4)*8+(s%4+2)%4]=0
                conf_temp[0][(s//4)*8+s%4]=1 
                return [conf_temp,ratio,occupy_index,W,u,dia]
                #break
            else:
                return "reject"
                #break
                
def E_parra_loc(conf,L,j):     
    total=0
    for i in range(L**2):        #iteration the cells
        total=total+conf[0][i*8+0]*conf[0][i*8+4]+conf[0][i*8+1]*conf[0][i*8+5]\
                   +conf[0][i*8+2]*conf[0][i*8+6]+conf[0][i*8+3]*conf[0][i*8+7]\
                   -conf[0][i*8+0]*conf[0][i*8+6]+conf[0][i*8+1]*conf[0][i*8+7]\
                   -conf[0][i*8+2]*conf[0][i*8+4]+conf[0][i*8+3]*conf[0][i*8+5]
    return total*j/8      #because each spin label "2",so need to divide 2       

def E_hop_loc():
    pass
def E_spin_loc():
    pass
                
samples=1 
hop_update=0
spin_update=0 
E_total=0
delta_mc=delta_md=delta_v=0
delta_mc_mc=delta_mc_md=delta_mc_v=0
delta_md_mc=delta_md_md=delta_md_v=0
delta_v_mc=delta_v_md=delta_v_v=0
delta_mc_H=delta_md_H=delta_v_H=0

S=np.zeros((3,3))
f=np.zeros((3,1))
#S00=S01=S02=S10=S11=S12=S20=S21=S22=0
#f0=f1=f2=0          
while True:
    try_hop=ele_hop(conf_new,L,mc,md,v)
    if try_hop !="reject":
        conf_new,ratio,occupy_index,W,u,dia=try_hop
        conf_total.append(conf_new.copy())
        samples=samples+1
        hop_update=hop_update+1
        E_hop_loc=-ratio      #local energy produced by hopping
        E_loc=E_parra_loc(conf_new,L,j)+E_hop_loc
        #E_loc=E_parra_loc(conf_new,L,j)+E_hop_loc+1/E_hop_loc
        
        delta_mc_loc=Delta_mc_loc(L,j,mc,md,v,u,dia,W,occupy_index)
        delta_md_loc=Delta_md_loc(L,j,mc,md,v,u,dia,W,occupy_index)
        delta_v_loc=Delta_v_loc(L,j,mc,md,v,u,dia,W,occupy_index)
        delta_mc_mc_loc=delta_mc_loc*delta_mc_loc
        delta_mc_md_loc=delta_mc_loc*delta_md_loc
        delta_mc_v_loc=delta_mc_loc*delta_v_loc
        delta_md_mc_loc=delta_md_loc*delta_mc_loc
        delta_md_md_loc=delta_md_loc*delta_md_loc
        delta_md_v_loc=delta_md_loc*delta_v_loc
        delta_v_mc_loc=delta_v_loc*delta_mc_loc
        delta_v_md_loc=delta_v_loc*delta_md_loc
        delta_v_v_loc=delta_v_loc*delta_v_loc
        delta_mc_H_loc=delta_mc_loc*E_loc
        delta_md_H_loc=delta_md_loc*E_loc
        delta_v_H_loc=delta_v_loc*E_loc
    else:
        conf_total.append(conf_new.copy())
        samples=samples+1
        E_loc=E_parra_loc(conf_new,L,j)    
        delta_mc_H_loc=delta_mc_loc*E_loc
        delta_md_H_loc=delta_md_loc*E_loc
        delta_v_H_loc=delta_v_loc*E_loc
    E_total=E_total+E_loc
    
    delta_mc=delta_mc+delta_mc_loc
    delta_md=delta_md+delta_md_loc
    delta_v=delta_v+delta_v_loc
    delta_mc_mc=delta_mc_mc+delta_mc_mc_loc
    delta_mc_md=delta_mc_md+delta_mc_md_loc
    delta_mc_v=delta_mc_v+delta_mc_v_loc
    delta_md_mc=delta_md_mc+delta_md_mc_loc
    delta_md_md=delta_md_md+delta_md_md_loc
    delta_md_v=delta_md_v+delta_md_v_loc
    delta_v_mc=delta_v_mc+delta_v_mc_loc
    delta_v_md=delta_v_md+delta_v_md_loc
    delta_v_v=delta_v_v+delta_v_v_loc
    delta_mc_H=delta_mc_H+delta_mc_H_loc
    delta_md_H=delta_md_H+delta_md_H_loc
    delta_v_H=delta_v_H+delta_v_H_loc   
    if samples==sample_goal:
        break
      
    try_spin=spin_flip(conf_new,L,mc,md,v)
    if try_spin !="reject":
        conf_new,ratio,occupy_index,W,u,dia=try_spin
        conf_total.append(conf_new.copy())
        samples=samples+1
        spin_update=spin_update+1
        E_spin_loc=0.5*j*ratio     #local energy produced by spin flip
        E_loc=E_parra_loc(conf_new,L,j)+E_spin_loc
        
        delta_mc_loc=Delta_mc_loc(L,j,mc,md,v,u,dia,W,occupy_index)
        delta_md_loc=Delta_md_loc(L,j,mc,md,v,u,dia,W,occupy_index)
        delta_v_loc=Delta_v_loc(L,j,mc,md,v,u,dia,W,occupy_index)
        delta_mc_mc_loc=delta_mc_loc*delta_mc_loc
        delta_mc_md_loc=delta_mc_loc*delta_md_loc
        delta_mc_v_loc=delta_mc_loc*delta_v_loc
        delta_md_mc_loc=delta_md_loc*delta_mc_loc
        delta_md_md_loc=delta_md_loc*delta_md_loc
        delta_md_v_loc=delta_md_loc*delta_v_loc
        delta_v_mc_loc=delta_v_loc*delta_mc_loc
        delta_v_md_loc=delta_v_loc*delta_md_loc
        delta_v_v_loc=delta_v_loc*delta_v_loc
        delta_mc_H_loc=delta_mc_loc*E_loc
        delta_md_H_loc=delta_md_loc*E_loc
        delta_v_H_loc=delta_v_loc*E_loc
    else:
        conf_total.append(conf_new.copy())
        samples=samples+1
        E_loc=E_parra_loc(conf_new,L,j)
        delta_mc_H_loc=delta_mc_loc*E_loc
        delta_md_H_loc=delta_md_loc*E_loc
        delta_v_H_loc=delta_v_loc*E_loc
    E_total=E_total+E_loc
    
    delta_mc=delta_mc+delta_mc_loc
    delta_md=delta_md+delta_md_loc
    delta_v=delta_v+delta_v_loc
    delta_mc_mc=delta_mc_mc+delta_mc_mc_loc
    delta_mc_md=delta_mc_md+delta_mc_md_loc
    delta_mc_v=delta_mc_v+delta_mc_v_loc
    delta_md_mc=delta_md_mc+delta_md_mc_loc
    delta_md_md=delta_md_md+delta_md_md_loc
    delta_md_v=delta_md_v+delta_md_v_loc
    delta_v_mc=delta_v_mc+delta_v_mc_loc
    delta_v_md=delta_v_md+delta_v_md_loc
    delta_v_v=delta_v_v+delta_v_v_loc
    delta_mc_H=delta_mc_H+delta_mc_H_loc
    delta_md_H=delta_md_H+delta_md_H_loc
    delta_v_H=delta_v_H+delta_v_H_loc 
    if samples==sample_goal:
        break
E=E_total/sample_goal
delta_mc=delta_mc/sample_goal
delta_md=delta_md/sample_goal
delta_v=delta_v/sample_goal
delta_mc_mc=delta_mc_mc/sample_goal
delta_mc_md=delta_mc_md/sample_goal
delta_mc_v=delta_mc_v/sample_goal
delta_md_mc=delta_md_mc/sample_goal
delta_md_md=delta_md_md/sample_goal
delta_md_v=delta_md_v/sample_goal
delta_v_mc=delta_v_mc/sample_goal
delta_v_md=delta_v_md/sample_goal
delta_v_v=delta_v_v/sample_goal
delta_mc_H=delta_mc_H/sample_goal
delta_md_H=delta_md_H/sample_goal
delta_v_H=delta_v_H/sample_goal



S[0][0]=delta_mc_mc-delta_mc*delta_mc+0.001
S[0][1]=delta_mc_md-delta_mc*delta_md
S[0][2]=delta_mc_v-delta_mc*delta_v
S[1][0]=delta_md_mc-delta_md*delta_mc
S[1][1]=delta_md_md-delta_md*delta_md+0.001
S[1][2]=delta_md_v-delta_md*delta_v
S[2][0]=delta_v_mc-delta_v*delta_mc
S[2][1]=delta_v_md-delta_v*delta_md
S[2][2]=delta_v_v-delta_v*delta_v+0.001
f[0][0]=delta_mc*E-delta_mc_H
f[1][0]=delta_md*E-delta_md_H
f[2][0]=delta_v*E-delta_v_H
x=np.linalg.solve(S,f)