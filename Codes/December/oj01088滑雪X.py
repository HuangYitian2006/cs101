dx=[1,-1,0,0]
dy=[0,0,1,-1]
m,n=map(int,input().split())
a=[[0 for i in range(n)]for j in range(m)]
dp=[1]*10001
position=[(-1,-1)]*10001
for i in range(m):
    a[i][0:n]=map(int,input().split())
for i in range(m):
    for j in range(n):
        position[a[i][j]]=(i,j)
print(position[0:26])
print(a)
for i in range(10000,-1,-1):
    if position[i]!=(-1,-1):
        for j in range(4):
            x,y=position[i][0],position[i][1]
            nx,ny=x+dx[j],y+dy[j]
            if 0<=nx<m and 0<=ny<n and a[nx][ny]>a[x][y]:
                dp[i]=max(dp[i],dp[a[nx][ny]]+1)
print(max(dp))
