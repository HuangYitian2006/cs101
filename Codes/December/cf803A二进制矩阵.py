import sys

n,k=map(int,input().split())
a=[[0]*n for i in range(n)]
r,c=0,0
if k>n**2:
    print(-1)
    sys.exit()
if k==1:
    a[0][0]=1
    k=0
while k>=2:
    if r==c:
        a[r][c]=1
        k-=1
        c+=1
    else:
        a[r][c],a[c][r]=1,1
        k-=2
        c+=1
    if c==n:
        r+=1
        c=r
if k:
    if a[r][r]==0:
        a[r][r]=1
    else:
        a[r+1][r+1]=1
for i in range(n):
    print(*a[i])
