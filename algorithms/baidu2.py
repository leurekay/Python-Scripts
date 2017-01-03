import math
while True:
    s=raw_input()
    sp_num=[]
    if s !="":
        m=int(s.split()[0])
        n=int(s.split()[1])
        for i in range(m,n+1):
            box=[]
            max_bit=int(math.log10(i))
            power=max_bit+1
            b=i
            while max_bit:
                a=b//(10**max_bit)
                b=b%(10**max_bit)
                box.append(a**power)
                if b<10:
                    box.append(b**power)
                    break
                else:
                    max_bit=max_bit-1
            if sum(box)==i:
                sp_num.append(i)
        if len(sp_num)==0:
            print 'none'
        else:
            for i in range(len(sp_num)):
                if i !=len(sp_num)-1 : 
                    print sp_num[i],
                else:
                    print sp_num[i]
    else:
        break
