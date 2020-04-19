while True:
    t=float(input())
    n=2
    if t==0:
        break
    while t>0:
        t-=1.0/n
        n+=1
    print(n-2,'card(s)')
