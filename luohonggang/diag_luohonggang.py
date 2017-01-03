# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:06:09 2016

@author: aa
"""

from sympy import *
init_printing(use_unicode=True)
t,f,j1,j2,c,d,sigma,v=symbols('t f j1 j2 c d sigma v')

A=Matrix([[j1*d*sigma/2,-t*f,j2*v/2,0],[-t*f,-j1*d*sigma/2,0,j2*v/2],
          [j2*v/2,0,-j1*c*sigma/2,0],[0,j2*v/2,0,j1*c*sigma/2]])
eig=A.diagonalize()
F1=c**2*j1**2*sigma**2/8 + d**2*j1**2*sigma**2/8 + f**2*t**2/2 + j2**2*v**2/4
F2=sqrt(c**4*j1**4*sigma**4 - 2*c**2*d**2*j1**4*sigma**4 - 8*c**2*f**2*j1**2*sigma**2*t**2 + 4*c**2*j1**2*j2**2*sigma**2*v**2 - 8*c*d*j1**2*j2**2*sigma**2*v**2 + d**4*j1**4*sigma**4 + 8*d**2*f**2*j1**2*sigma**2*t**2 + 4*d**2*j1**2*j2**2*sigma**2*v**2 + 16*f**4*t**4 + 16*f**2*j2**2*t**2*v**2)/8
a=simplify(F2**2-F1**2)