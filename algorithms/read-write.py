# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:47:48 2016

@author: aa
"""
import time
f = open('C:/Users/aa/Documents/Python Scripts/algorithms/test.txt', 'w')

now=time.strftime("%Y-%m-%d %H:%M:%S")
f.write("hello")
for i in range(20):
    f.write("hello,%dday\n"%(i))
f.close()