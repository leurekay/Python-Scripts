# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:19:10 2016
  the initial configuration of some fixed T is 
the end of last T
@author: aa
"""

from __future__ import division
import random,math,time
import numpy as np
import matplotlib.pyplot as plt
import pylab
start_time=time.time()
L=50

Low=0.1
High=7
Interval=0.1
mc_steps=12000
T_list=np.arange(Low,High,Interval)
T_list=np.append(T_list,np.arange(1.7,2.7,0.01))
T_list.sort()
steps=mc_steps*L**2

        
m_list=[]
Cv_list=[]
conf=np.random.choice((-1,1),(L,L))
M=0
E=0
for i in range(L):
    for j in range(L):
        M=M+conf[i][j]
        E=E-0.5*conf[i][j]*sum([conf[(i-1)%L][j],conf[(i+1)%L][j],conf[i][(j-1)%L],conf[i][(j+1)%L]])
for T in T_list:
    
    M_total=0    
    E2_total=0
    E_total=0
    
    sample=0
    for step in range(steps):    
        s=[random.randrange(L),random.randrange(L)]
        x,y=s
        neighbour=[conf[(x-1)%L][y],conf[(x+1)%L][y],conf[x][(y-1)%L],conf[x][(y+1)%L]]
        delta_E=2*conf[x][y]*sum(neighbour)
        rho=min(1,math.exp(-delta_E/T))
        if random.random()<rho:
            conf[x][y]=-1*conf[x][y]
            M=M+2*conf[x][y]
            E=E+delta_E
        if step>steps/2 and step%(L**2)==0:
        #if step>steps/2 :
            sample=sample+1
            M_total=M_total+M
            E_total=E_total+E
            E2_total=E2_total+E**2
    m=M_total/sample/L**2
    E_mean=E_total/sample
    E2_mean=E2_total/sample
    Cv=(E2_mean-E_mean**2)/T**2/L**2
    m_list.append(abs(m))  
    Cv_list.append(Cv)
#maxCv=max(Cv_list)
#Cv_list=[i*1.2/maxCv for i in Cv_list]
run_time=time.time()-start_time    
#plt.figure(figsize=(20,10))
#plt.plot(T_list,m_list,color="blue",linewidth=1.5,label="mc")    
#plt.savefig('L=%d'%L)
pylab.figure(figsize=(40,20),dpi=800)
pylab.title('$%i\\times%i$ lattice' % (L, L),fontsize=40)
pylab.xlabel('$T$', fontsize=30)
pylab.ylabel('$<|M|>/N$', fontsize=30)
pylab.plot(T_list, m_list, 'bo-', clip_on=False)
pylab.plot(T_list, Cv_list, 'ro-', clip_on=False)
pylab.ylim(0.0, 2)
pylab.savefig('L=%i,mc_steps=%d,Low=%.1f,High=%.1f,Interval=%.1f,time=%.2f.png' % (L,mc_steps,Low,High,Interval,run_time))
print run_time
