# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:19:36 2016

@author: aa
"""

from sympy import *
#init_printing(use_unicode=True)
ep,j1,j2,c,d,sigma,v=symbols('ep j1 j2 c d sigma v')

A=Matrix([[ep,j1*d*sigma/2,j2*v/2,0],[j1*d*sigma/2,-ep,0,j2*v/2],
          [j2*v/2,0,0,-j1*c*sigma/2],[0,j2*v/2,-j1*c*sigma/2,0]])
eig=A.diagonalize()