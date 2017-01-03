# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 13:53:45 2016

@author: aa
"""
import copy
import numpy as np
import random
L=50
def generate(L):
    A=np.zeros((L+1,L+1),"int")
    for i in range(1,L+1):
        a=np.arange(1,L+1,1)
        random.shuffle(a)
        for j in range(1,L+1):
            A[i][j]=a[j-1]
            A[i][0]=0
    return A
M=generate(L) 
F=generate(L)
M_old=copy.copy(M)
F_old=copy.copy(F)
def fuck(i):
    if M[i][0]==0:
        if F[M[i][1]][0]==0:
            F[M[i][1]][0]=i
            M[i][0]=M[i][1]
        elif list(F[M[i][1],:]).index(i)< list(F[M[i][1],:]).index(F[M[i][1]][0]):
            M[F[M[i][1]][0]][0]=0
            F[M[i][1]][0]=i
            M[i][0]=M[i][1]
            
        else:
            temp=M[i][1]
            for j in range(1,L):
                M[i][j]=M[i][j+1]
            M[i][L]=temp  

while True:
    flag=0
    for i in range(1,L+1):
        if M[i][0]==0:
            fuck(i)
        else:
            flag=flag+1
    if flag==L:
        break
    
for i in range(1,L+1):
    print "%d---%d"%(i,M[i][0]) 

        