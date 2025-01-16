import sys

sys.setrecursionlimit(200000000)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
mx=float('inf')
n=0
def ts(x,y):
    a[x][y]='2'
    for i in range(4):
        if a[x+dx[i]][y+dy[i]]=='1':
            ts(x+dx[i],y+dy[i])

def dfs(x,y,step):
    #print(x,y)
    global mx,n
    if a[x][y]=='1':
        mx=min(step,mx)
        return
    if step>=mx or step>2*n-3:
        return
    v[x][y] = 1
    for i in range(4):
        if 1<=x+dx[i]<=n and 1<=y+dy[i]<=n and v[x+dx[i]][y+dy[i]]==0:
            if a[x+dx[i]][y+dy[i]]=='2':
                dfs(x+dx[i],y+dy[i],0)
            elif a[x+dx[i]][y+dy[i]]!='2':
                dfs(x + dx[i], y + dy[i], step+1)
    v[x][y]=0



n=int(input())
a=[['0' for i in range(n+2)]for j in range(n+2)]
v=[[0 for i in range(n+2)]for j in range(n+2)]
for i in range(1,n+1):
    a[i][1:n+1]=input()
# print(a)
fl=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]=='1':
            ts(i,j)
            fl=1
            break
    if fl:
        break
# print(a)
fl=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j] == '2':
            dfs(i, j,0)
            fl = 1
            break
    if fl:
        break
print(mx-1)