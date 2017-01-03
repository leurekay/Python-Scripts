# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:04:38 2016

@author: aa
"""

import multiprocessing
import os
import time
from multiprocessing import Process, Queue



COUNT=500000
def count1(n):
    m=1
    while n>0:
        n-=1
        m=2*m
    print 'ax'

def process_job(n):
    local_time=time.time()
    #t=Process(target=count,args=(COUNT//n,)) 
    t = Process(target=count, args=(COUNT//n,))
    t.start()
    t.join()
    print time.time()-local_time

#if __name__=='main':
#for i in [1,2,4,6]:
 #   process_job(i)
local_time=time.time()
#t=Process(target=count,args=(COUNT//n,)) 
t = Process(target=count, args=(COUNT//1,))
t.start()
t.join()
print time.time()-local_time
