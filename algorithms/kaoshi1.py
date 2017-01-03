# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:43:56 2016

@author: aa
"""
import numpy as np
Te=input()
while True:
    Te=Te-1
    n=input()
    m=input()
    M=np.zeros((n,m),dtype='int')
    flag=0
    while n:
        n=n-1
        x1=raw_input()
        x=x1.split()
        for i in range(m):
            M[flag][i]=int(x[i])
        flag=flag+1
box=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(m):
            for l in range(k+1,m):
                total=total+M[i]
