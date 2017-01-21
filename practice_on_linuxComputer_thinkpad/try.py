while 1:
    
    num=[1,2,3,4]
    eng=['one','two','three','four']
    try:
        
        a=input('enter:')
        b=num.index(a)
    except ValueError:
        print 'the number you enter in not in zhe list'
        continue

    c=eng[b]
    print c
