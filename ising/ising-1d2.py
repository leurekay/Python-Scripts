# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:36:58 2016

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

T_list=np.arange(0.1,10,0.2)
def Tm(h):    
    m_list=[]
    for T in T_list:
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
   
    h_color={0.5:'ro-',1:'yo-',2:'bo-',4:'go-',8:'co-',16:'ko-'}
    
    pylab.title('$%i\\times%i$ lattice' % (L, L))
    pylab.xlabel('$T$', fontsize=16)
    pylab.ylabel('$<|M|>/N$', fontsize=16)
    for h in h_color:
        pylab.plot(T_list, Tm(h), h_color[h], clip_on=False)
    pylab.ylim(0, 1)
    pylab.savefig('L=%i,mc_steps=%d,time=%.2f.png' % (L,mc_steps,run_time))
    run_time=time.time()-start_time
    print run_time