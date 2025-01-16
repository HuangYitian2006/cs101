while True:
    n = int(input())
    if n == 0:
        break
    t = list(map(int, input().split()))
    k = list(map(int, input().split()))
    t.sort()
    k.sort()
    tl,tr,kl,kr,s=0,n-1,0,n-1,0
    while tl<=tr:
        if t[tr]>k[kr]:
            s+=1
            tr-=1
            kr-=1
        elif t[tl]>k[kl]:
            s+=1
            tl,kl=tl+1,kl+1
        else:
            s+=-1 if t[tl]<k[kr] else 0
            tl+=1
            kr-=1
    print(200*s)
