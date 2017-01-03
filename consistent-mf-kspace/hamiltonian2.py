# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 20:17:41 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy 

def hamiltonian(j,mc,md,v,kx,ky,sigma):
    h=np.zeros((4,4),dtype='complex')
    h[0][2]=h[2][0]=h[1][3]=h[3][1]=j*v/2
    h[0][0]=j*md*sigma/2
    h[1][1]=-j*md*sigma/2
    h[2][2]=-j*mc*sigma/2
    h[3][3]=j*mc*sigma/2
       
    #luo hong gang
    h[0][1]=-np.exp(-kx*1j)-2*np.exp(0.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    h[1][0]=-np.exp(kx*1j)-2*np.exp(-0.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    #h[0][1]=-h[0][1]
    #h[1][0]=-h[1][0]
    # leggett
    #h[0][1]=-np.exp(-kx*1j)-2*np.exp(1.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    #h[1][0]=-np.exp(kx*1j)-2*np.exp(-1.5*kx*1j)*cos(0.5*sqrt(3)*ky)
    #geim
    #h[0][1]=2*cos(sqrt(3)*ky)+4*cos(sqrt(3)*0.5*ky)*cos(1.5*kx)
    #h[1][0]=2*cos(sqrt(3)*ky)+4*cos(sqrt(3)*0.5*ky)*cos(1.5*kx)
    
    dia,u=np.linalg.eig(h)
    idx = dia.argsort() 
    dia = dia[idx]
    u = u[:,idx]
    ut=u.transpose()
    ud=np.conjugate(ut)
    return [h,dia,u,ud]
   
def order(L,j,mc,md,v):
    mc_all=0
    md_all=0
    v_all=0
    E_all=0
    kx_range=2*pi/3*np.linspace(0,2-2/L,2*L-1)
    #divid_ky=0    
    for sigma in [-1,1]:
        divid_ky=0
        for kx in kx_range:
            kxmid=2*pi*(1-1/L)/3
            if kx<=kxmid:
                divid_ky=divid_ky+1
                heigh=kx*sqrt(3)
            else:
                divid_ky=divid_ky-1
                heigh=(2*pi*(2-2/L)/3-kx)*sqrt(3)
            ky_range=np.linspace(-heigh,heigh,divid_ky)
            for ky in ky_range:
     
                h,dia,u,ud=hamiltonian(j,mc,md,v,kx,ky,sigma)
                mc_all=mc_all+sigma*(u[0][0]*ud[0][0]+u[0][1]*ud[1][0])
                md_all=md_all+sigma*(u[2][0]*ud[0][2]+u[2][1]*ud[1][2])
                if sigma==1:
                    v_all=v_all+u[2][0]*ud[0][0]+u[2][1]*ud[1][0]
                if sigma==-1:
                    v_all=v_all+u[0][0]*ud[0][2]+u[0][1]*ud[1][2]
                E_all=E_all+dia[0]+dia[1]
                    
    mc=mc_all/L**2/(-2)   
    md=md_all/L**2/2         
    v=-v_all/L**2
    E=E_all/L**2
    return [mc,md,v,E]
         
if __name__=='__main__' :
    L=7
    j=1.6
    mc=0.01
    md=0.01
    v=0.83
    flag=0
    while True:
        flag=flag+1
        print flag,'mc:',mc,'md:',md, 'v:',v
        new_mc,new_md,new_v,E=order(L,j,mc,md,v)
        if abs(mc-new_mc)<0.001 and abs(md-new_md)<0.001 and abs(v-new_v)<0.001:
            break
        else:
            mc=new_mc
            md=new_md
            v=new_v
    print new_mc
    print new_md
    print new_v
    
    kx_range=2*pi/3*np.linspace(0,2-2/L,2*(L-1)+1)
    #divid_ky=0   
    scatter_x=[]
    scatter_y=[]
    for sigma in [-1,1]:
        divid_ky=0
        for kx in kx_range:
            kxmid=2*pi*(1-1/L)/3
            if kx<=kxmid:
                divid_ky=divid_ky+1
                heigh=kx*sqrt(3)
            else:
                divid_ky=divid_ky-1
                heigh=(2*pi*(2-2/L)/3-kx)*sqrt(3)
            ky_range=np.linspace(-heigh,heigh,divid_ky)
            for ky in ky_range:
                scatter_x.append(kx)
                scatter_y.append(ky)
     
    f=plt.figure(figsize=(8,8))
    plt.scatter(scatter_x,scatter_y)
    plt.xlim(0,8)
    plt.ylim(-4,4)