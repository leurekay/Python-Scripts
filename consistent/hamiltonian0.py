from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt


L=8
j=1.3
mc=0.6
md=0.4
v=0.6

down=lambda i:(i+L)%(L**2)
left=lambda i:L*(i//L-(i-1)//L)+i-1
def H():
    h=np.zeros((8*L**2,8*L**2))
    for i in range(L**2):
        print i
        h[i*8][i*8+1]=h[i*8][8*left(i)+1]=h[i*8][8*down(i)+1]=-1
        h[i*8+1][i*8]=h[8*left(i)+1][i*8]=h[8*down(i)+1][i*8]=-1
        h[i*8+2][i*8+3]=h[i*8+2][8*left(i)+3]=h[i*8+2][8*down(i)+3]=-1
        h[i*8+3][i*8+2]=h[8*left(i)+3][i*8+2]=h[8*down(i)+3][i*8+2]=-1

        h[i*8+6][i*8+2]=h[i*8+0][i*8+4]=h[i*8+4][i*8+0]=h[i*8+2][i*8+6]=j*v/2
        h[i*8+7][i*8+3]=h[i*8+1][i*8+5]=h[i*8+5][i*8+1]=h[i*8+3][i*8+7]=j*v/2

        h[i*8+4][i*8+4]=h[i*8+6][i*8+6]=-j*mc/2
        h[i*8+0][i*8+0]=h[i*8+2][i*8+2]=j*md/2
        h[i*8+5][i*8+5]=h[i*8+7][i*8+7]=j*mc/2
        h[i*8+1][i*8+1]=h[i*8+3][i*8+3]=-j*md/2
        
    return h
        
if __name__=='__main__' :
    a=H()






        
