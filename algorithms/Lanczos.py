# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:12:43 2016

@author: aa
"""
from __future__ import division
import numpy as np
N=900
A=np.random.random_integers(1,6,(N,N))
dia,u=np.linalg.eig(A)


v=np.random.random_integers(1,6,(N,1))
v=v/(np.dot(v.T,v))**0.5
for i in range(50):
    v=np.dot(A,v)
    print i  
v=v/(np.dot(v.T,v))**0.5