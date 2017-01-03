while True:
    a=[]
    s=raw_input()
    if s !="":
        n=int(s.split()[0])
        m=int(s.split()[1])
        temp=n**2
        for i in range(m):
            temp=temp**0.5
            a.append(temp)
        print '%.2f'%sum(a)
    else:
        break
