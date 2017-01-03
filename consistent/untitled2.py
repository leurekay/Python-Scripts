# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:26:52 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt

a=np.array([[1,0,2],[0,-1,5],[2,5,3]])
d=np.linalg.eig(a)
print a
print d
print '<><><><>)(<>_+>##$%@@'
lam=np.array([[6.86214033,0,0],[0,0.7571417,0],[0,0,-4.61928203]])
u=np.array([[ 0.27665062,  0.93900388, -0.20429428],
       [ 0.51568807, -0.32445431, -0.79296609],
       [ 0.81088239, -0.11402244,  0.57399358]])
ut=u.transpose()

w=np.dot(ut,np.dot(a,u))
v1=np.array([0.27665062,0.51568807,0.81088239,])

values,vectors=np.linalg.eig(a)
idx = values.argsort() 
values = values[idx]
vectors = vectors[:,idx]


