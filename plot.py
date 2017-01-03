# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:39:43 2016

@author: aa
"""

import matplotlib.pyplot as plt
import numpy as np

def plot2D():
plt.figure(figsize=(20,10))
plt.plot(x,y1,color="blue",linewidth=1.5,label="mc")
plt.plot(x,y2,"r",label="md",linewidth=1.5)
plt.plot(x,y3,"g",label="v",linewidth=1.5)
#plt.plot(x,y4,"y",label="E",linewidth=1)
plt.xlabel("j",fontsize= 'xx-large')
plt.ylabel("order", fontsize= 'xx-large')
plt.title("cell:%d*%d ,j_step:%.2f"%(L,L,j_step),fontsize= 'xx-large')
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

plt.figure(figsize=(20,10))
plt.plot(x,y4,"y",label="E",linewidth=2)
plt.xlabel("j",fontsize= 'xx-large')
plt.ylabel("E",fontsize= 'xx-large')
plt.title("cell:%d*%d"%(L,L),fontsize= 'xx-large')