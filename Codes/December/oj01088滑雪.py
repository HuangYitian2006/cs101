dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y):
    if v[x][y]==1:
        return dp[x][y]
    v[x][y]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<m and 0<=ny<n and a[nx][ny]<a[x][y]:
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

m,n=map(int,input().split())
a=[[0 for i in range(n)]for j in range(m)]
v=[[0 for i in range(n)]for j in range(m)]
dp=[[1 for i in range(n)]for j in range(m)]
for i in range(m):
    a[i][0:n]=map(int,input().split())
mx=0
for i in range(m):
    for j in range(n):
        if v[i][j]==0:
            dfs(i,j)
            mx=max(mx,dp[i][j])
print(mx)
