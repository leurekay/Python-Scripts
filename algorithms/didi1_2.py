# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:44:17 2016

@author: aa
"""

import sys
for s in sys.stdin:
    a=[]
    b=''
    m=int(s.split()[0])
    n=int(s.split()[1])
    while m/n :
        a.append(m%n)
        m=m/n
    a.append(m)
    for i in range(len(a)):
        if a[i]==10:
            a[i]='A'
        elif a[i]==11:
            a[i]='B'
        elif a[i]==12:
            a[i]='C'
        elif a[i]==13:
            a[i]='D'
        elif a[i]==14:
            a[i]='E'
        elif a[i]==15:
            a[i]='F'
    for i in range(len(a)):
        b=b+str(a[len(a)-1-i]) 
    print b
