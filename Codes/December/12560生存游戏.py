n,m=map(int,input().split())
a=[['0' for i in range(m+2)]for j in range(n+2)]
b=[['0' for i in range(m)]for j in range(n)]
dx=[0,0,1,-1,-1,-1,1,1]
dy=[1,-1,0,0,-1,1,-1,1]
for i in range(n):
    a[i+1][1:m+1]=input().split()
for i in range(1,n+1):
    for j in range(1,m+1):
        s=0
        for k in range(8):
            nx,ny=i+dx[k],j+dy[k]
            s+=int(a[nx][ny])
        if a[i][j]=='1':
            if s==2 or s==3:
                b[i-1][j-1]='1'
        else:
            if s==3:
                b[i - 1][j - 1] = '1'
for i in range(n):
    print(*b[i])