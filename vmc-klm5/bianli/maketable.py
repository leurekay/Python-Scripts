# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:42:43 2016

@author: aa
"""
from __future__ import division
import xlrd
import matplotlib.pyplot as plt
import pylab

data = xlrd.open_workbook("L2W9000N7000.xlsx")
table=data.sheets()[0]
j=table.col_values(0)
E=table.col_values(1)
Omc=table.col_values(3)
Omd=table.col_values(4)
Ov=table.col_values(5)

j.pop(0)
E.pop(0)
Omc.pop(0)
Omd.pop(0)
Ov.pop(0)

Ov1=[Ov[i]/j[i] for i in range(len(Ov))]
#Omc=[i*2 for i in Omc]
#Omd=[i*2 for i in Omd]
h_color={"E":'ro-',"mc":'yo-',"md":'bo-',"v":'go-',8:'co-',16:'ko-'}
    
#pylab.title('$%i\\times%i$ lattice' % (L, L))

plt.figure(1)
pylab.title("lattice:2*2  warm-up:9000 sample:7000")
pylab.xlabel('$j$', fontsize=16)
pylab.ylabel('$order$', fontsize=16)

pylab.plot(j, Omc,'b^-', clip_on=False,label='mc')
pylab.plot(j, Omd, 'y*-', clip_on=False,label="md")
pylab.plot(j, Ov, 'ro-', clip_on=False,label="v")
pylab.xlim(0, 3.8)
pylab.ylim(0,1)
pylab.legend()
pylab.savefig("a")
plt.figure(2)
pylab.title("lattice:2*2  warm-up:9000 sample:7000")
pylab.xlabel('$j$', fontsize=16)
pylab.ylabel('$E$', fontsize=16)
pylab.plot(j, E, 'co-', clip_on=False,label="E")
pylab.ylim(-1.5,-0.7)
pylab.legend()
pylab.savefig("b")
