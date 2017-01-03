# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:40:56 2016

@author: aa
"""
import numpy as np

try:
    
    a=4/0
except ZeroDivisionError,d:
    a="infinty"

A=np.array([[1,2],[2,4]])
#Ainv=np.linalg.inv(A)
try:
    
    Ainv=np.linalg.inv(A)
except np.linalg.linalg.LinAlgError as err:
    if 'Singular matrix' in err.message:
        Ainv="uninvers"
        
    