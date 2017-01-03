# -*- coding: utf-8 -*-
"""
Created on Wed May 04 14:44:26 2016

@author: aa
"""

from sympy import *
init_printing(use_unicode=True)
k,c,d,v,j,f1,f2,eps,lam,e=symbols('k c d v j f1 f2 eps lam e')
f1=j**2*(0.25+0.11**2*j**2)/4+j**2*v**2/2+eps**2



k=-j**4*0.11*2
w=4*(0.11**2*j**6/16+0.11*j**5*v**2/16+j**4*v**4/16)
cha=sqrt(w) + eps*k/(2*sqrt(w)) - eps**2*k**2/(8*w**(3/2))
fun0=eps*sqrt(f1+cha)
E=-2*integrate(fun0,(eps,0,1))+j*v**2

E2=E.subs(v,1-1**2/4/j**2)
aa=solve(E2,j)