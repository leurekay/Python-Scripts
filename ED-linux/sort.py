from __future__ import division
import math

def supplus(a,b):
    if type(b)==list:
        box=[]
        for i in range(len(b)):
            box.append(a+b[i])
        return box
    else:
        return a+b
def suplist(a,b):
    if type(a)==list and type(b)==list:
        box=[]
        for i in range(len(a)):
            box.append(a[i])
        for j in range(len(b)):
            box.append(b[j])
        return box
    elif type(a)==list and type(b)!=list:
        box=[]
        for i in range(len(a)):
            box.append(a[i])
        box.append(b)
        return box
    elif type(b)==list and type(a)!=list:
        box=[]
        for i in range(len(b)):
            box.append(b[i])
        box.append(a)
        return box
    else:
        return [a,b]

def f(L,n):
    if L==n and n!=0:
        return 2**n-1
    elif n==0:
        return 0
    else:
        return suplist(supplus(2**(L-1),f(L-1,n-1)),f(L-1,n))

def pair1(L,n):
    confs=f(L,n)
    confs.sort()
    step=len(confs)
    box=[]
    while (step):
        step=step-1
        for i in confs:
            if i !=confs[step]:
                distance=abs(i-confs[step])
                x=math.log(distance)/math.log(2)
                if x.is_integer() or distance==2**(L-1)-1:
                    box.append((confs[step],i))
    return box
def pair(L,n):
    confs=f(L,n)
    confs.sort()
    step=len(confs)
    box=[]
    while (step):
        step=step-1
        for i in range(len(confs)):
            if i !=step:
                distance=abs(confs[i]-confs[step])
                x=math.log(distance)/math.log(2)
                if x.is_integer() or distance==2**(L-1)-1:
                    box.append((step,i))
    return box

if __name__=="__main__":
    a= pair(3,1)
    b= pair(2,1)
                

    

