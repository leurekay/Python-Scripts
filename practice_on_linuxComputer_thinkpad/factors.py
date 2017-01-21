import time
def multiply(x):
    numlist=[]
    flag=0  
    a=int(pow(x,0.5))
    if (x==2)or(x==3):
        flag=1
        numlist.append(x)
        return numlist
    else:
        while (x%a) :
            a=a-1
            if (a==1) :
                numlist.append(x)
                flag=1
                return numlist
                break  
    if flag==0 :
        return multiply(a)+multiply(x/a)
    
while 1:
    num=int(input('enter:'))
    start1=time.clock()
    print multiply(num)
    end1=time.clock()
    print 'running time: %.7f s' %(end1-start1)
    f=open(str(num),'w')
    f.write(str(multiply(num))+'\n')
    f.write('running time: %.7f s' %(end1-start1))
    f.close()
    
            
        
    
    
