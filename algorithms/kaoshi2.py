# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:12:53 2016

@author: aa
"""

Te=input()
while True:
    Te=Te-1
    n=input()
    x1=raw_input()
    y1=raw_input()
    x=x1.split()
    for i in range(n):
        x[i]=int(x[i])
        
    y=y1.split()
    for i in range(n-1):
        y[i]=int(y[i])
    sp=sum(x)-sum(y)
    print sp