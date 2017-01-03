# -*- coding: utf-8 -*-
"""
Created on Tue May 03 19:46:40 2016

@author: aa
"""

from sympy import *
init_printing(use_unicode=True)
c,d,v,j,f1,f2,eps,lam,e=symbols('c d v j f1 f2 eps lam e')
d=1/2
c=0.11*j
f1=j**2*(d**2+c**2)/4+j**2*v**2/2+eps**2
f2=sqrt(f1**2-4*j**4*(d**2*c**2/16+d*c*v**2/8+v**4/16))
e0=-(sqrt(f1+f2)+sqrt(f1-f2))/(sqrt(2))
e=e0.subs(lam,1)
E0=2*integrate(e*eps,(eps,0,1))+2*j*d*c

fun=diff(E,v)
#fun2=fun.subs(v,1-lam**2/4/j**2)
fun2=fun.subs(v,1-1**2/4/j**2)
w=solve(fun2,j)