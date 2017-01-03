from __future__ import division
import math
import numpy as np
from sort import *


def block(n_up,L):
    #n_up spin-up electrons occupy in L sites
    n_down=L-n_up
    dim=(math.factorial(L)/math.factorial(L-n_up)/math.factorial(n_up))**2
    h=np.zeros((dim,dim))
    dim_up=dim_down=int(math.factorial(L)/math.factorial(L-n_up)/math.factorial(n_up))
    hop_up=pair(L,n_up)     #all the hopping pairs
    hop_down=pair(L,n_down)
    pair_len=len(hop_up)
    for i in range(dim_up):
        for item in hop_down:
            h[item[0]+i*dim_up][item[1]+i*dim_up]=-1
    for i in range(dim_down):
        for item in hop_up:
            h[item[0]*dim_up+i][item[1]*dim_up+i]=-1
    dia,u=np.linalg.eig(h)
    dia.sort()
    print h
    return min(dia)

L=6
box=[]
for i in range(1,L//2+1):
    print i
    box.append(block(i,L))

E_min= min(box)

#a=block(1,5)
#dia,u=np.linalg.eig(a)
#dia.sort()

#b=np.array([[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]])
#dia1,u1=np.linalg.eig(b)
