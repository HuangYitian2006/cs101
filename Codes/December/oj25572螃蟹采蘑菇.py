from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(x1,y1,x2,y2,step):
    q=deque()
    q.append((x1,y1,x2,y2,step))
    while q:
        x1, y1, x2, y2, step=q.popleft()
        #print(x1,y1)
        if (x1,y1)==(tx,ty) or (x2,y2)==(tx,ty):
            return step
        for i in range(4):
            nx1,ny1,nx2,ny2=x1+dx[i],y1+dy[i],x2+dx[i],y2+dy[i]
            if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n and v1[nx1][ny1]==v2[nx2][ny2]==0:
                s=a[nx1][ny1]+a[nx2][ny2]
                if s==0 or s==9 or s==5 or s==14:
                    q.append((nx1,ny1,nx2,ny2,step+1))
                    v1[nx1][ny1]=1
                    v2[nx2][ny2]=1
    return -1

n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
v1=[[0 for i in range(n)]for j in range(n)]
v2=[[0 for i in range(n)]for j in range(n)]
s1x,s1y,s2x,s2y,tx,ty=1,1,1,1,1,1
f=0
for i in range(n):
    for j in range(n):
        if a[i][j]==9:
            tx,ty=i,j
        elif a[i][j]==5 and f==0:
            s1x,s1y=i,j
            f=1
        elif a[i][j]==5 and f==1:
            s2x,s2y=i,j
print('yes' if bfs(s1x,s1y,s2x,s2y,0)>=0 else 'no')