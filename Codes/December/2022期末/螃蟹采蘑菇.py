from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
sx1,sy1,sx2,sy2,tx,ty=0,0,0,0,0,0
f=0
for i in range(n):
    for j in range(n):
        if a[i][j]==5 and f==0:
            sx1,sy1=i,j
            f=1
        elif a[i][j]==5 and f==1:
            sx2,sy2=i,j
        elif a[i][j]==9:
            tx,ty=i,j
v=[[0]*n for i in range(n)]
q=deque()
q.append((sx1,sy1,sx2,sy2))
v[sx1][sx1]=1
flag=0
while q:
    x1,y1,x2,y2=q.popleft()
    if (x1,y1)==(tx,ty) or (x2,y2)==(tx,ty):
        flag=1
        break
    for i in range(4):
        nx1,ny1,nx2,ny2=x1+dx[i],y1+dy[i],x2+dx[i],y2+dy[i]
        if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n and v[nx1][ny1]==0:
            if a[nx1][ny1] in (0,5,9) and a[nx2][ny2] in (0,5,9):
                v[nx1][ny1]=1
                q.append((nx1,ny1,nx2,ny2))
print('yes'if flag else 'no')
