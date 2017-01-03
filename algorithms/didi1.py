# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:12:11 2016

@author: aa
"""

#coding = utf-8


while True:
    a=[]
    b=''
    s=raw_input() 
    m=int(s.split()[0])
    n=int(s.split()[1])
    while m/n :
        a.append(m%n)
        m=m/n
    a.append(m)
    for i in range(len(a)):
        if a[len(a)-1-i]==10:
            a[len(a)-1-i]='A'
        elif a[len(a)-1-i]==11:
            a[len(a)-1-i]='B'
        elif a[len(a)-1-i]==12:
            a[len(a)-1-i]='C'
        elif a[len(a)-1-i]==13:
            a[len(a)-1-i]='D'
        elif a[len(a)-1-i]==14:
            a[len(a)-1-i]='E'
        elif a[len(a)-1-i]==15:
            a[len(a)-1-i]='F'
        b=b+str(a[len(a)-1-i]) 
    print b
