sx=float('inf')
s=-1
d=[[-1,0],[1,0],[0,-1],[0,1]]
def dfs(x,y):
    global sx,s
    if a[x][y]=='2':
        return
    s+=1
    if a[x][y]=='1':
        sx=min(sx,s)
        s-=1
        return
    a[x][y]='2'
    for i in range(4):
        dfs(x+d[i][0],y+d[i][1])
    s-=1
    a[x][y]='0'


n,m=map(int,input().split())
a=[['2' for i in range(m+2)]for j in range(n+2)]
for i in range(1,n+1):
    a[i][1:m+1]=input().split()
dfs(1,1)
print(sx if sx!=float('inf') else 'NO')