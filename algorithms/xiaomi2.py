# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 19:03:22 2016

@author: aa
"""

while True:
    a=''
    s=raw_input()
    if s !="":
        #n=int(s.split()[0])
        #m=int(s.split()[1])
        b=s.split()
        lenth=len(b)
        for i in range(lenth):
            if i==lenth-1:
                a=a+str(b[lenth-1-i])
            else:
                a=a+str(b[lenth-1-i])+' '
        print a
    else:
        break