from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(int(input())):
    n,m,t=map(int,input().split())
    sx,sy,ex,ey=0,0,0,0
    a=[]
    for i in range(n):
        a.append(input())
    q=deque()
    for i in range(n):
        for j in range(m):
            if a[i][j]=='S':
                sx,sy=i,j
            if a[i][j]=='E':
                ex,ey=i,j
    v=[[[0 for i1 in range(t)]for i2 in range(m)]for i3 in range(n)]
    q.append((0,sx,sy))
    flag=0
    while q:
        step,x,y=q.popleft()
        #print(step,x,y)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny]=='E':
                    print(step+1)
                    flag = 1
                elif (a[nx][ny]!='#' or step%t==t-1) and v[nx][ny][step%t]==0:
                    q.append((step+1,nx,ny))
                    v[nx][ny][step % t]=1
        if flag:
            break
    if flag==0:
        print('Oop!')

