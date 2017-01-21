def f(x):
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
