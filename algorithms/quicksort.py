# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 20:55:52 2016

@author: aa
"""
import random
import copy
def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L
def randQuickSort(L,i,j):
    pivot=random.randint(0,len(L)-1)
    #i=0
    #j=len(L)-1
    while i != j:
        while L[j]>L[pivot]:
            if i==j:
                break
            j=j-1
        while L[i]<L[pivot] or L[i]==L[pivot]:
            if i==j:
                break
            i=i+1
        L[i],L[j]=L[j],L[i]
    randQuickSort(L,i,j)
    randQuickSort(L,i,j)

def insertSort(L):
    len_L=len(L)
    for i in range(1,len_L):
        while i:
            if L[i] < L[i-1]:
                L[i-1],L[i]=L[i],L[i-1]
                i=i-1
            else:
                break
    return L
    
    
#L=[5,0,4,6,8,7,1,3,4,6,12,4,654,354,4,5,7,6,9,6,6,54,7,3,8]
Lold=[random.randint(1,7777777) for i in range(8888888)]
L=copy.copy(Lold)
#Lnew=quickSort(L, 0, len(L)-1)
L_loc=L.sort
#b=insertSort(L)
