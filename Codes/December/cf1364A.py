for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    l,r=0,n-1
    ans=n
    if s%x!=0:
        print(n)
        continue
    mx=0
    while l<=n-1:
        if a[l]%x!=0:
            mx=max(n-l-1,l+1)
            break
        l+=1
    while r>=0:
        if a[r]%x!=0:
            mx=max(mx,n-r,r)
            break
        r-=1
    if mx==0:
        print('-1')
    else:
        print(mx)
