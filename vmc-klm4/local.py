# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:14:46 2016

@author: aa
"""
from __future__ import division
import numpy as np
from mfh import *

def Delta_mc_loc(L,j,mc,md,v,U,dia,W,occupy_index):
    U_t=U.T
    U_d=U_t.conjugate()
    v_mc=V_mc(L,j,mc,md,v)
    Q_mc=np.zeros((8*L**2,8*L**2),dtype='complex')
    Q_mc_nominator=np.dot(U_d,np.dot(v_mc,U))
    for i in range(4*L**2,8*L**2):
        for j in range(4*L**2):
            Q_mc[i][j]=Q_mc_nominator[i][j]/(dia[j]-dia[i])
    A_mc=np.dot(np.dot(U,Q_mc),U_d)
    total=0
    for beta in range(4*L**2):
        for j in range(8*L**2):
            total=total+A_mc[occupy_index[beta]][j]*W[j][beta]
    return total

def Delta_md_loc(L,j,mc,md,v,U,dia,W,occupy_index):
    U_t=U.T
    U_d=U_t.conjugate()
    v_md=V_md(L,j,mc,md,v)
    Q_md=np.zeros((8*L**2,8*L**2),dtype='complex')
    Q_md_nominator=np.dot(U_d,np.dot(v_md,U))
    for i in range(4*L**2,8*L**2):
        for j in range(4*L**2):
            Q_md[i][j]=Q_md_nominator[i][j]/(dia[j]-dia[i])
    A_md=np.dot(np.dot(U,Q_md),U_d)
    total=0
    for beta in range(4*L**2):
        for j in range(8*L**2):
            total=total+A_md[occupy_index[beta]][j]*W[j][beta]
    return total
    
def Delta_v_loc(L,j,mc,md,v,U,dia,W,occupy_index):
    U_t=U.T
    U_d=U_t.conjugate()
    v_v=V_v(L,j,mc,md,v)
    Q_v=np.zeros((8*L**2,8*L**2),dtype='complex')
    Q_v_nominator=np.dot(U_d,np.dot(v_v,U))
    for i in range(4*L**2,8*L**2):
        for j in range(4*L**2):
            Q_v[i][j]=Q_v_nominator[i][j]/(dia[j]-dia[i])
    A_v=np.dot(np.dot(U,Q_v),U_d)
    total=0
    for beta in range(4*L**2):
        for j in range(8*L**2):
            total=total+A_v[occupy_index[beta]][j]*W[j][beta]
    return total

def SR(delta_mc_loc,delta_md_loc,delta_v_loc,E_loc):
    delta_mc_mc_loc=delta_mc_loc*delta_mc_loc
    delta_mc_md_loc=delta_mc_loc*delta_md_loc
    delta_mc_v_loc=delta_mc_loc*delta_v_loc
    delta_md_mc_loc=delta_md_loc*delta_mc_loc
    delta_md_md_loc=delta_md_loc*delta_md_loc
    delta_md_v_loc=delta_md_loc*delta_v_loc
    delta_v_mc_loc=delta_v_loc*delta_mc_loc
    delta_v_md_loc=delta_v_loc*delta_md_loc
    delta_v_v_loc=delta_v_loc*delta_v_loc
    delta_mc_H_loc=E_loc
    