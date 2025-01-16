import sys

dx=[-1,-1,-1,0,0,1,1,1]
dy=[1,-1,0,1,-1,1,-1,0]
sys.setrecursionlimit(1<<30)
def dfs(x,y):
    a[x][y]='.'
    for i in range(8):
        if a[x+dx[i]][y+dy[i]]=='W':
            dfs(x+dx[i],y+dy[i])
n,m=map(int,input().split())
a=[['.'for i in range(m+2)]for j in range(n+2)]
for i in range(1,n+1):
    a[i][1:m+1]=input()
ans=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]=='W':
            ans+=1
            dfs(i,j)
print(ans)