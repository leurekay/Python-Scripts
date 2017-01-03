# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:55:27 2016
consider the period bounday condition,
map the boundary site to the right site 
@author: aa
"""

def middle(cell,L):
    return cell
    
def left(cell,L):
    if cell%L==0:
        return cell+L-1
    else:
        return cell-1
def down(cell,L):
    if L**2-cell<L+1:
        return cell+L-L**2
    else:
        return cell+L
def right(cell,L):
    if (cell+1)%L==0:
        return cell+1-L
    else:
        return cell+1
def up(cell,L):
    if cell<L:
        return cell+L**2-L
    else:
        return cell-L
        
if __name__=='__main__' :
    L=4
    print down(12,L)