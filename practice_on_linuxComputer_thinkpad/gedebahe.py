import time
def judge(x):
    flag=1
    a=int(pow(x,0.5))
    while (x%a):
        a=a-1
        if a==1:
            flag=1
            break
    if a>1 :
        flag=0
    return flag

while 1:
    
    num=input('enter:')
    start1=time.clock()
    list1=[2]+range(3,num/2,2)
    for i in list1:
        if judge(i) and judge(num-i) :
            pass #print '%d + %d = %d' %(i,(num-i),num)
    end1=time.clock()

    print '***********************************************************'
    print '***********************************************************'
    print '***********************************************************'
    print '***********************************************************'
    print '***********************************************************'
    
    start2=time.clock()
    for j in range(2,num/2,1):
        if judge(j) and judge(num-j) :
           pass # print '%d + %d = %d' %(j,(num-j),num)
    end2=time.clock()
    
    print 'running time: %.7f s' %(end1-start1)    
    print 'running time: %.7f s' %(end2-start2) 



