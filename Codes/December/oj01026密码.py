def findcir(st,n):
    ret=[]
    for i in range(n):
        x=a[i]
        cnt=1
        while x!=i:
            x=a[x]
            cnt+=1
        ret.append(cnt)
    return ret
def move(st,t):
    for i in range(t):
        st=a[st]
    return st
while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    for i in range(n):
        a[i]-=1
    cir=findcir(a,n)
    while True:
        c=input().split(' ',1)
        k=int(c[0])
        if k==0:
            break
        d=c[1].ljust(n)
        ans=['']*n
        for i in range(n):
            ans[move(i,k%cir[i])]=d[i]
        print(''.join(ans))
    print()
