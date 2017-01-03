import random
import copy
def sort(L):
    i=0
    # i:sear even  j:search odd
    j=len(L)-1
    while i != j:
        while L[j]%2==0:
            if i==j:
                break
            j=j-1
        
        while L[i]%2 :
            if i==j:
                break
            i=i+1
        L[i],L[j]=L[j],L[i]

#L=[5, 4, 5, 7, 1, 6, 10, 10]
while True:
    L=[random.randint(1,10) for i in range(20)]
    Lold=copy.copy(L)
    sort(L)
    print L
