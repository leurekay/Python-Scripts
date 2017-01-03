# -*- coding: utf-8 -*-
"""
Created on Tue May 03 18:56:45 2016

@author: aa
"""

import numpy as np
import matplotlib.pyplot as plt
import random  ,math
from pylab import *

x=np.arange(-2,2,0.05)
y=(sqrt(4*x**2+x**4/4)-x**2/2)/8
fy=lambda a: (sqrt(4*a**2+a**4/4)-a**2/2)/8
z=fy(0.5)/0.5*x
f1=plt.figure(figsize=(24,15))
plt.plot(x,y,linewidth="1")
plt.plot(x,z,'g',linewidth="1")
#plt.plot(x,z,"g",label="$sin(x)/x$",linewidth="3")
plt.ylim(0,1)
plt.xlim(0,1)
plt.legend()

plt.show()
print fy(0.5)/0.5