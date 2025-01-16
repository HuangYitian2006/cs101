d=[[-1,0],[1,0],[0,-1],[0,1]]
ans,a,v,tmp=[],[],[],[]
sx=-float('inf')
def dfs(x,y,s):
    global ans,sx,tmp
    if not(0<=x<=n-1 and 0<=y<=m-1):
        return
    if v[x][y]:
        return
    s+=a[x][y]
    tmp.append([x,y])
    if x==n-1 and y==m-1:
        if s>sx:
            ans=tmp[:]
            sx=s
        tmp.pop()
        return
    v[x][y]=1
    for i in range(4):
        dfs(x+d[i][0],y+d[i][1],s)
    tmp.pop()
    v[x][y]=0




n,m=map(int,input().split())
v=[[0 for i in range(m)]for j in range(n)]
for _ in range(n):
    a.append(list(map(int,input().split())))
dfs(0,0,0)
for i in range(len(ans)):
    print(ans[i][0]+1,ans[i][1]+1)
#print(sx)