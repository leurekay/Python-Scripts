# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 14:14:21 2016

@author: aa
"""
import sys
a=(1,2,0)
print sys.getrefcount((1,2,0))
b=(1,2,0)
print sys.getrefcount((1,2,0))