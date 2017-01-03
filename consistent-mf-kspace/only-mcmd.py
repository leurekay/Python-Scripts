# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 15:43:14 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 

def hamiltonian(j,mc,md,kx,ky,sigma):
    h=np.zeros((4,4),dtype='complex')
    h[0][0]=j*md*sigma/2
    h[1][1]=-j*md*sigma/2
    h[2][2]=-j*mc*sigma/2
    h[3][3]=j*mc*sigma/2
       
    
    h[0][1]=-np.exp(-kx*1j)-2*np.exp(0.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    h[1][0]=-np.exp(kx*1j)-2*np.exp(-0.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    
    dia,u=np.linalg.eig(h)
    idx = dia.argsort() 
    dia = dia[idx]
    u = u[:,idx]
    ut=u.transpose()
    ud=np.conjugate(ut)
    return [h,dia,u,ud]
   
def order(L,j,mc,md):
    mc_all=0
    md_all=0
   
    for sigma in [-1,1]:
        for kx in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/L):
            for ky in np.arange(-pi/sqrt(3),pi/sqrt(3),2*pi/sqrt(3)/L):
                h,dia,u,ud=hamiltonian(j,mc,md,kx,ky,sigma)
                mc_all=mc_all+sigma*(u[0][0]*ud[0][0]+u[0][1]*ud[1][0])
                md_all=md_all+sigma*(u[2][0]*ud[0][2]+u[2][1]*ud[1][2])
                
                
                    
    mc=mc_all/L**2/(-2)   
    md=md_all/L**2/2         
    
    return [mc,md]
         
if __name__=='__main__' :
    L=20
    j=1.5
    mc=0.01
    md=0.01
    kx=0.1
    ky=0.5
    sigma=1
    m=hamiltonian(j,mc,md,kx,ky,sigma)
    flag=0
    while True:
        flag=flag+1
        print flag,'mc:',mc,'md:',md
        new_mc,new_md=order(L,j,mc,md)
        if abs((mc-new_mc)/mc)<0.00001 and abs((md-new_md)/md)<0.0001:
            break
        else:
            mc=new_mc
            md=new_md
           
    print new_mc
    print new_md
    mc1=lambda j:(sqrt(4*2.33**2+0.25*j**2)-0.5*j)*j/8/2.33**2
    print mc1(j)