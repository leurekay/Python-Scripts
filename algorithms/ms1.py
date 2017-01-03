# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:09:12 2016

@author: aa
"""

while True:
    try:
        N=input()
        A=raw_input()
        B=A.split()
        C = [int(x) for x in B]
        odd=0        
        for i in range(N):
            if C[i]%2==1:
                odd=odd+1
        even=N-odd
        print odd-even
                
    except EOFError:
        break
