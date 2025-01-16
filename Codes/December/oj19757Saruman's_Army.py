while True:
    d,n=map(int,input().split())
    if d==n==-1:
        break
    a=list(map(int,input().split()))
    a.sort()
    curl,cur=a[0],a[0]
    ans=1
    for i in range(1,n):
        #print(cur,curl)
        if a[i]>cur+d:
            ans+=1
            curl,cur=a[i],a[i]
        elif a[i]<=curl+d:
            cur=a[i]
    print(ans)