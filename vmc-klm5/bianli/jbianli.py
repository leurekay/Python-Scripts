# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:45:26 2016

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
import xlwt

L=3
j=3
mc=0.15
md=0.05
v=1.4
Nwarmup=6000
Nstep=5000
LOOP=1

j_list=[0.4,0.8,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.2,2.4]
j_list=[0.1,0.2,0.6,1.25,1.35,1.45,1.55,1.65,1.75,2.6,2.8,3]
#j_list=[0.1,0.2,0.6,1.25]
#j_list=[1.35,1.45,1.55,1.65]
j_list=[0.3,1.6,1.8,3]
jlistStr=""
for i in j_list:
    jlistStr=jlistStr+"-"+str(i)
mcL=0
mcH=1
mdL=0
mdH=1
vL=0
vH=2
Piece=4
oddtable=[1,3,5,7]
Dic={1:"Eele",2:"variance",3:"Omc",4:"Omd",5:"Ov",6:"mcVar",7:"mdVar",8:"vVar",9:"acc",10:"accH",11:"accS"}

FileName="L"+str(L)+"W"+str(Nwarmup)+"N"+str(Nstep)+jlistStr+'.xls'





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
    
    M=u[:,np.arange(0,L*L*4,1)]
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
    Esquare_total1=0
    Esquare_total2=0
    Esquare_total3=0
    
    while True: 
        loop=LOOP
        while loop:
            loop=loop-1   
            for i in range(3*L**2):
                try_hop=ele_hop(conf_new,L,mc,md,v,u)
                if try_hop != "reject":
                    ratio,conf_new=try_hop
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
    
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    f = open('j='+str(j)+'a.txt', 'a+')
    f.write("E_cell1=%.3f E_cell2=%.3f E_cell3=%.3f E_cell=%.3f Nstep=%d  L=%d  j=%.2f  mc=%.2f  md=%.2f  v=%.2f  run_time=%.1fs  "%(E_cell1,E_cell2,E_cell3,E_cell,Nstep,L,j,mc,md,v,run_time)+now+"\n\n")
    f.close()
    return [E_ele,variance,(OmcA+OmcB)/2,(OmdA+OmdB)/2,(Ov+Ov1)/2,acc,accHop,accSpin]



SecretBox=[]
f=xlwt.Workbook()
tableAll=f.add_sheet('jorder')


for j in j_list:    
    bianli=1
    Emin=999999
    BigData=[]
    while True:
        mc_range=np.arange(mcL,mcH,(mcH-mcL)/(2*Piece))
        md_range=np.arange(mdL,mdH,(mdH-mdL)/(2*Piece))
        v_range=np.arange(vL,vH,(vH-vL)/(2*Piece))
        mc_range=mc_range[oddtable,]
        md_range=md_range[oddtable,]
        v_range=v_range[oddtable,]        
        for mc in mc_range:
            for md in md_range:
                for v in v_range:
                    E_ele,variance,Omc,Omd,Ov,acc,accHop,accSpin=measure(L,j,mc,md,v)
                    E_ele=E_ele.real
                    if abs(variance)>0.0001 or E_ele<-5:
                        E_ele=E_ele+1000   
                    if E_ele<Emin:
                        Emin=E_ele
                        VarPara=[mc,md,v]
                        Data=(E_ele,variance,Omc,Omd,Ov,mc,md,v,acc,accHop,accSpin)
                    BigData.append((E_ele,variance,Omc,Omd,Ov,mc,md,v,acc,accHop,accSpin))
        mcL=VarPara[0]-(mcH-mcL)/Piece
        mcH=VarPara[0]+(mcH-mcL)/Piece
        mdL=VarPara[1]-(mdH-mdL)/Piece
        mdH=VarPara[1]+(mdH-mdL)/Piece
        vL=VarPara[2]-(vH-vL)/Piece
        vH=VarPara[2]+(vH-vL)/Piece
        if mcL<0:
            mcL=0
        if mdL<0:
            mdL=0
        if vL<0:
            vL=0
        if bianli== 4:
            break
        bianli=bianli+1
    SecretBox.append(Data)
    
    table=f.add_sheet("j="+str(j))
    for i in range(len(Data)):
        table.write(0,i+1,Dic[i+1])
    for i in range(len(BigData)):
        for j in range(len(Data)):
            table.write(i+1,j+1,str(BigData[i][j]))
    f.save(FileName)

for i in range(len(Data)):
    tableAll.write(0,i+1,Dic[i+1])
for i in range(len(j_list)):
    tableAll.write(i+1,0,j_list[i])
f.save(FileName)


for i in range(len(SecretBox)):
    for j in range(len(Data)):
        tableAll.write(i+1,j+1,str(SecretBox[i][j]))
f.save(FileName)