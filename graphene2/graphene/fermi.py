# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:39:14 2016

@author: aa
"""

from __future__ import division
import random,copy,time
import numpy as np
from math import *

L=40
N=L*L
kx_range=2*pi/3*np.linspace(0,2-2/L,2*(L-1)+1)
boxE=[]
boxkx=[]
boxky=[]
fill=1.05
divid_ky=0
Ekxky=np.zeros((3,L*L),"float")
i=0
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
        E=-sqrt(1+4*cos(1.5*kx)*cos(sqrt(3)*ky/2)+4*(cos(sqrt(3)*ky/2))**2)
        #boxE.append(E)
        #boxkx.append(kx)
        #boxky.append(ky)
        Ekxky[0][i]=-2*cos(kx)-2*cos(ky)
        Ekxky[1][i]=kx
        Ekxky[2][i]=ky
        i=i+1
#Ekxky=np.zeros((3,len(boxE)),"float")  
E_arr=Ekxky[0,:]
inx=E_arr.argsort()
Ekxky=Ekxky[:,inx]
E_fermi=Ekxky[0][N*fill/2]
print E_fermi
#f1 = plt.figure(1)  
#plt.subplot(211) 
plt.figure(figsize=(8,8))
plt.xlim(xmax=5,xmin=-5)
plt.ylim(ymax=5,ymin=-5)
plt.scatter(Ekxky[1,0:N*fill/2],Ekxky[2,0:N*fill/2])

plt.savefig("/home/gates/hp/vmc-1dchain/feimi/fill_"+str(fill)+".jpg")


