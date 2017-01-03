# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:38:36 2016

@author: aa
"""

Te=input()
while Te:
    Te=Te-1
    n=input()
    x1=raw_input()
    y1=raw_input()
    if x1 !="":
        x=x1.split()
        for i in range(n):
            x[i]=int(x[i])
    else:
        break
    if y1 !="":
        y=y1.split()
        for i in range(n-1):
            y[i]=int(y[i])
    else:
        break
    sp=sum(x)-sum(y)
    print sp