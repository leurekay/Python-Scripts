# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:37:39 2016

@author: aa
"""

from __future__ import division
from math import *
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-1.5,1.5,0.01)
y=1-0.25/x/x
z=(np.exp(x/3)-np.exp(-x/3))/(np.exp(x/3)+np.exp(-x/3))
plt.figure(figsize=(16,8))
plt.plot(x,y,label=".",color="blue",linewidth=2)
plt.plot(x,z,"r",label="$cos(x^2)$")

plt.xlabel("mc")
plt.ylabel("E")
plt.title("E-mc")
plt.xlim(0,1.5)
plt.ylim(-0.1,2)
plt.legend()
plt.show()

