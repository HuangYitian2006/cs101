for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s,ans=0,0
    ps=set()
    for i in range(n):
        s+=a[i]
        if s==0 or s in ps:
            ans+=1
            s=0
            ps.clear()
        else:
            ps.add(s)
    print(ans)