d=[[-1,-2],[-1,2],[-2,-1],[-2,1],[1,2],[1,-2],[2,-1],[2,1]]
s0=0
def dfs(x,y,s):
    global s0
    if x<0 or y<0 or x>=n or y>=m:
        return
    if v[x][y]:
        return
    if s==m*n:
        s0+=1
        return
    v[x][y]=1
    for i in range(8):
        dfs(x+d[i][0],y+d[i][1],s+1)
    v[x][y]=0

for _ in range(int(input())):
    n,m,x0,y0=map(int,input().split())
    v=[[0 for i in range(m)]for j in range(n)]
    s0=0
    dfs(x0,y0,1)
    print(s0)