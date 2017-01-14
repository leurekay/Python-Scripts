# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 19:56:09 2017

@author: aa
"""
from math import *
import matplotlib.pyplot as plt
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=Point(0,0)

def arrow(f,p,angle):
    A=Point(p.x+0.5*cos(pi+angle),p.y+0.5*sin(pi+angle))
    B=Point(p.x+0.5*cos(angle),p.y+0.5*sin(angle))   
    ArrAngle=pi/10
    ArrLen=0.1
    ArrAngle_absolute1=pi+angle-ArrAngle
    ArrAngle_absolute2=pi+angle+ArrAngle
    C1=Point(B.x+ArrLen*cos(ArrAngle_absolute1),B.y+ArrLen*sin(ArrAngle_absolute1))
    C2=Point(B.x+ArrLen*cos(ArrAngle_absolute2),B.y+ArrLen*sin(ArrAngle_absolute2))
    #plt.figure(figsize=(6,6))
    plt.plot([A.x,B.x,C1.x,C2.x,B.x],[A.y,B.y,C1.y,C2.y,B.y],"g")
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    
f=plt.plot(figsize=(10,10))
ax = plt.gca()
ax.set_aspect(1)
arrow(f,p1,pi/3)
arrow(f,p1,pi/4)
plt.savefig("a")
