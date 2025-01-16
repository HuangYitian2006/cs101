from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
mx=float('inf')
q=deque()
def ts(x,y):
    a[x][y]='2'
    q.append((x,y,0))
    v[x][y] = 1
    for i in range(4):
        if a[x+dx[i]][y+dy[i]]=='1':
            ts(x+dx[i],y+dy[i])


def bfs():
    global mx,n,q
    while q:
        x,y,step=q.popleft()
        if a[x][y]=='1':
            mx=min(step,mx)
            return
        for i in range(4):
            if 1<=x+dx[i]<=n and 1<=y+dy[i]<=n and v[x+dx[i]][y+dy[i]]==0:
                q.append((x + dx[i], y + dy[i], step+1))
                v[x + dx[i]][y + dy[i]]=1



n=int(input())
a=[['0' for i in range(n+2)]for j in range(n+2)]
v=[[0 for i in range(n+2)]for j in range(n+2)]
for i in range(1,n+1):
    a[i][1:n+1]=input()
fl=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]=='1':
            ts(i,j)
            fl=1
            break
    if fl:
        break
bfs()
print(mx-1)