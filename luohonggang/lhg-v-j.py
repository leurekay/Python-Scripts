# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:39:42 2016

@author: aa
"""

from sympy import *
#init_printing(use_unicode=True)
y,j,v,lam,=symbols("y j v lam")
Eg=y-((y-2)**3-y**3)/3/(1-y)
partial=diff(Eg,y)
a=solveset(partial,y)
E=j*v**2-((lam**2+j**2*v**2)**1.5-j**3*v**3)*4/3/lam**2
diffE=diff(E,v)
b=solve(diffE,v)