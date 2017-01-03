# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 18:27:08 2016

@author: aa
"""

import numpy as np
#A=np.random.randint(0,3,(20000,20000))
#dia,u=np.linalg.eig(A)
L=12
n=5
a=np.array(())
total=0
for i in range(L-n+1):
    for j in range(i+1,L-n+2):
        for k in range(j+1,L):
            print i,j,k
            total=total+1