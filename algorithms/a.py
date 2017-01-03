# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:07:51 2016

@author: aa
"""
import numpy as np
from scipy import linalg

def exchange(x,y):
    temp=x
    x=y
    y=temp
    
a=5
b=2    
exchange(a,b)
print 'a=%d\nb=%d'%(a,b)
print id(a)