# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:39:14 2016

@author: aa
"""

from __future__ import division
import random,copy,time
import numpy as np
from math import *

L=4
kx_range=2*pi/3*np.linspace(0,2-2/L,2*(L-1)+1)
boxE=[]
boxkx=[]
boxky=[]
nc=1
n=nc/2
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
        E=-sqrt(1+4*cos(1.5*kx)*cos(sqrt(3)*ky/2)+4*(cos(sqrt(3)*ky/2))**2)
        boxE.append(E)
        boxkx.append(kx)
        boxky.append(ky)
  
    