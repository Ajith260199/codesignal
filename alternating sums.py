def alternatingSums(a):
    t1 =[]
    t2 = []
    for i in range(len(a)):
        if i%2==0:
            print(i)
            t1.append(a[i])
        elif i%2!=0:
            t2.append(a[i])
    a=[sum(t1)]
    b=[sum(t2)]
    return a+b
            
