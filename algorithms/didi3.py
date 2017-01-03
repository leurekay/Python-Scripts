# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 17:51:51 2016

@author: aa
"""
from __future__ import division
import math
a=[0,4/52]
total=4/52
for i in range(2,50):
    f=a[i-1]*(50-i)/(53-i)
    a.append(f)
    total=total+f*i
print total,sum(a)
bb=(math.atan(0.5)+math.atan(1/3)+math.atan(1))*180/(math.pi)