# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:44:21 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
from  Halmiltonian import *

L=3
j=1.3
mc=0.6
md=0.4
v=0.6
    
a=H(L,j,mc,md,v)
w=np.linalg.eig(a)
