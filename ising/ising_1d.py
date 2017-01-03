# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:51:27 2016
H=-j*∑ Si*Sj - ∑ h*Si
@author: aa
"""
from __future__ import division
import random,math,time
import numpy as np
import matplotlib.pyplot as plt
import pylab
start_time=time.time()
L=20          #链长

T=5    #温度
mc_steps=10000
steps=mc_steps*L

h_list=np.arange(-20,20,1)    
m_list=[]
for h in h_list:
    conf=[random.choice((-1,1)) for i in range(L)]
    M=sum(conf)
    M_total=0
    sample=0
    for step in range(steps):
        
        s=random.randrange(L)
        neighbour=[conf[(s-1)%L],conf[(s+1)%L]]
        delta_E=2*conf[s]*sum(neighbour)+2*conf[s]*h
        rho_ratio=min(1,math.exp(-delta_E/T))
        if random.random()<rho_ratio:
            conf[s]*=-1
            M=M+conf[s]*2
        if step>steps/2 and step%(L)==0:
            M_total=M_total+M
            sample=sample+1
    m=M_total/sample/L
    m_list.append(m) 
            
#plt.figure(figsize=(20,10))
#plt.plot(h_list,m_list,color="blue",linewidth=1.5,label="mc")    
#plt.savefig('L=%d'%L)

pylab.title('$%i\\times%i$ lattice' % (L, L))
pylab.xlabel('$T$', fontsize=16)
pylab.ylabel('$<|M|>/N$', fontsize=16)
pylab.plot(h_list, m_list, 'bo-', clip_on=False)
pylab.ylim(-1, 1)
#pylab.savefig('L=%i,mc_steps=%d,Low=%.1f,High=%.1f,Interval=%.1f,time=%.2f.png' % (L,mc_steps,Low,High,Interval,run_time))
run_time=time.time()-start_time
print run_time