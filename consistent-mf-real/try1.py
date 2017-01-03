# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:56:25 2016
实验，虚数
@author: aa
"""
from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 

A=np.array([[2,1+2j],[1-2j,3]])
dia,u=np.linalg.eig(A)

