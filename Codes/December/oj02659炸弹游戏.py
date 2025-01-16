m,n,k=map(int,input().split())
a=[[0]*n for i in range(m)]
for _ in range(k):
    r,s,p,t=map(int,input().split())
    for i1 in range(max(r-1-p//2,0),min(r+p//2,m)):
        for i2 in range(max(s-1-p//2,0),min(s+p//2,n)):
            a[i1][i2]+=1 if t else -1
    #print(a)
mx=-float('inf')
for i in range(m):
    mx=max(mx,max(a[i]))
ans=0
for i in range(m):
    for j in range(n):
        if a[i][j]==mx:ans+=1
print(ans)