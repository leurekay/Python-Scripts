# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:07:40 2016

@author: aa
"""

from __future__ import division
import random
import numpy as np

def conf_initial(L,N_up):
    conf=np.zeros((1,2*L),'int')   
    ele=random.sample(range(L),N_up)+random.sample(range(L,2*L),L-N_up) #2*L*l electron sit on 4*L*L location
    ele.sort()
    for i in ele:            #initial elctron
        conf[0][i]=1
    
    return conf

if __name__=='__main__' :   
    L=4
    N_up=1
    site=L*L*2   
    cong=conf_initial(L,N_up)