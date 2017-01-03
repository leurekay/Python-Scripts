# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:37:50 2016
initializing a random configuration
"1"label electron
"2"label local spin
@author: aa
"""
from __future__ import division
import random
import numpy as np

def conf_initial(L):
    conf=np.zeros((1,8*L*L),'int')   
    ele=random.sample(range(L*L*4),L*L*2) #2*L*l electron sit on 4*L*L location
    ele.sort()
    for i in ele:            #initial elctron
        conf[0][(i//4)*8+i%4]=1
    for i in range(L*L):    #initial onsite spin
        conf[0][8*i+4+random.randint(0,1)*2]=2
        conf[0][8*i+5+random.randint(0,1)*2]=2
    return conf

if __name__=='__main__' :   
    L=2
    cell=L*L
    site=L*L*2   