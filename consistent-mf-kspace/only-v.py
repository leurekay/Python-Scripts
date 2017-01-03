# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 14:12:21 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 

def hamiltonian(j,v,kx,ky,sigma):
    h=np.zeros((4,4),dtype='complex')
    h[0][2]=h[2][0]=h[1][3]=h[3][1]=j*v/2
    
    h[0][1]=-np.exp(-kx*1j)-2*np.exp(0.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    h[1][0]=-np.exp(kx*1j)-2*np.exp(-0.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    
    dia,u=np.linalg.eig(h)
    idx = dia.argsort() 
    dia = dia[idx]
    u = u[:,idx]
    ut=u.transpose()
    ud=np.conjugate(ut)
    return [h,dia,u,ud]
   
def order(L,j,v):
    v_all=0
    for sigma in [-1,1]:
        for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/L):
            for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/L):
                h,dia,u,ud=hamiltonian(j,v,kx,ky,sigma)
                if sigma==1:
                  
                    v_all=v_all+(u[2][0]*ud[0][0]+u[2][1]*ud[1][0]) 
                if sigma==-1:
                    v_all=v_all+(u[0][0]*ud[0][2]+u[0][1]*ud[1][2])
                  
    v=-v_all/L**2
    return v
         
if __name__=='__main__' :
    L=20
    j=1.9
    v=0.5
    flag=0
    while True:
        flag=flag+1
        print flag, 'v:',v
        new_v=order(L,j,v)
        if  v-new_v<0.00002:
            break
        else:
            
            v=new_v
    
    print new_v