t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    v=[(a[i],i) for i in range(n)]
    v.sort()
    b.sort()
    z=[0]*n
    for i in range(n):
        z[v[i][1]]=b[i]
    print(*z)