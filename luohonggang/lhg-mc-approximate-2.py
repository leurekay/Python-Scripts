# -*- coding: utf-8 -*-
"""
Created on Tue May 03 21:27:20 2016

@author: aa
"""
from sympy import *
init_printing(use_unicode=True)
c,d,v,j,f1,f2,eps,lam,e=symbols('c d v j f1 f2 eps lam e')
C=j**2*(0.25+0.11**2*j**2)/4+j**2*v**2/2
+2*sqrt(0.11**2*j**6/16+0.11*j**5*v**2/16+j**4*v**4/16)

E=sqrt(C**3-(1+C)**3)*2/3+j*v**2

fun=diff(E,v)

fun2=fun.subs(v,1-1**2/4/j**2)
w=solve(fun2,j)