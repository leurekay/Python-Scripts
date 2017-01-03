# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:07:40 2016

@author: aa
"""

from __future__ import division
import random
import numpy as np

def conf_initial(L):
    conf=np.zeros((1,2*L*L),'int')   
    ele=random.sample(range(L*L),int(L*L/2))+random.sample(range(L*L,2*L*L),int(L*L/2)) #2*L*l electron sit on 4*L*L location
    ele.sort()
    for i in ele:            #initial elctron
        conf[0][i]=1
    
    return conf

if __name__=='__main__' :   
    L=4
    cell=L*L
    site=L*L*2   
    cong=conf_initial(4)