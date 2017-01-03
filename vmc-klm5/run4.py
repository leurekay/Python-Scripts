# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 14:44:39 2016
在run3的基础上增加了防死循环机制，即：
在格点数比较少的时候，有时候不幸分配到了一种构型，不存在
另一个proposed构型，它们之间存在着自旋翻转或电子hopping的关系。
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
j=1
mc=0.4
md=0.4
v=0.5
steps=2000
sample_goal=steps*L**2
conf_new=conf_initial(L)
conf_new=np.array([[0, 1, 1, 0, 2, 0, 0, 2, 1, 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0,
        0, 2, 0, 1, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 2, 0, 0, 2, 1, 0, 1, 0,
        2, 0, 0, 2, 1, 0, 1, 0, 2, 0, 0, 2, 0, 1, 0, 1, 2, 2, 0, 0, 1, 0,
        0, 1, 2, 0, 0, 2, 1, 1, 1, 0, 2, 0, 0, 2, 1, 1, 1, 1, 2, 0, 0, 2,
        0, 1, 1, 0, 2, 0, 0, 2, 0, 0, 1, 0, 2, 0, 0, 2, 0, 1, 0, 0, 2, 0,
        0, 2, 0, 1, 1, 0, 2, 0, 0, 2, 1, 1, 1, 1, 2, 0, 0, 2]])


conf_total=[conf_new.copy()]
print conf_new




def ele_hop(conf_new,L,mc,md,v,u):
    flag=0
    while True:
        flag=flag+1
        if flag==100:
            return "reject"
        s_ele_index=random.randrange(0,4*L**2)  #index of ele in 4*L**2
        cell=s_ele_index//4   #index of cell
        s_conf_index=cell*8+s_ele_index%4
        if conf_new[0][s_conf_index]==0:    #judge the site wheather occupy
            continue
        A_B=(s_ele_index%4)%2       #0:A   1:B
        Up_Down=(s_ele_index%4)//2   #0:up  1:down      
        neigh_cell_index=[middle(cell,L),left(cell,L),down(cell,L)]
        neigh_allconf_index=[]
        for i in neigh_cell_index:
            neigh_allconf_index.append(i*8+2*Up_Down+1-A_B)
        neigh_occupy=[]
        for i in neigh_allconf_index:
            if conf_new[0][i] ==0:
                neigh_occupy.append(i)
        if len(neigh_occupy) !=0:
            break
    hop_conf_index=random.choice(neigh_occupy)
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
        #E_total=E_total+E_parra_loc(conf_new,L,j)+E_loc_hop(conf_new,L,j,mc,md,v,u)+E_loc_spin(conf_new,L,j,mc,md,v,u)
        E_total=E_total+E_parra_loc(conf_new,L,j)+E_loc_hop(conf_new,L,j,mc,md,v,u)
        if samples==sample_goal:
            break
    try_spin=spin_flip(conf_new,L,mc,md,v,u)
    if try_spin != "reject":
        ratio,conf_new=try_spin
        conf_total.append(conf_new.copy())
        samples=samples+1
        sample_spin=sample_spin+1
        #E_total=E_total+E_parra_loc(conf_new,L,j)+E_loc_hop(conf_new,L,j,mc,md,v,u)+E_loc_spin(conf_new,L,j,mc,md,v,u)
        E_total=E_total+E_parra_loc(conf_new,L,j)+E_loc_hop(conf_new,L,j,mc,md,v,u)
        if samples==sample_goal:
            break
E=E_total/samples
E_cell=E/L**2

run_time=time.time()-start_time 
print "run time:%d seconds"%run_time   

f = open('C:/Users/aa/Documents/Python Scripts/vmc-klm5/log.txt', 'a+')
now=time.strftime("%Y-%m-%d %H:%M:%S")
f.write("E=%.3f  E_cell=%.3f  steps=%d  L=%d  j=%.2f  mc=%.2f  md=%.2f  v=%.2f  run_time=%.1fs  "%(E,E_cell,steps,L,j,mc,md,v,run_time)+now+"\n\n")
f.close()
