# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:21:50 2016

@author: aa
"""

def jizhi(L):
    temp=699999
    for i in range(1,len(L)-2):
        if L[i]<L[i-1] and L[i]<L[i+1] and L[i]<temp:
           temp=i
    return temp
L=[9,8,7,5,6,7,9,8,9,5,2,3,2,1,2,3]
print jizhi(L)