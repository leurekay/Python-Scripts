# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:04:50 2016
when temperature T is fixed,plot h-m
@author: aa
"""

from __future__ import division
import random,math,time
import numpy as np
import matplotlib.pyplot as plt
import pylab
start_time=time.time()
L=18
mc_steps=10000
steps=mc_steps*L

h_list=np.arange(-20,20,1)
def hm(T):    
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
    return m_list        

if __name__=='__main__':
   
    T_color={0.5:'ro-',2:'yo-',4:'bo-',8:'go-',16:'co-',24:'ko-'}
    
    pylab.title('$%i\\times%i$ lattice' % (L, L))
    pylab.xlabel('$h$', fontsize=16)
    pylab.ylabel('$<|M|>/N$', fontsize=16)
    for T in T_color:
        pylab.plot(h_list, hm(T), T_color[T], clip_on=False)
    pylab.ylim(-1, 1)
    pylab.savefig('h-m;L=%i,mc_steps=%d,time=%.2f.png' % (L,mc_steps,run_time))
    run_time=time.time()-start_time
    print run_time