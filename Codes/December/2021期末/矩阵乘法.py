n,m1,m2=map(int,input().split())
a=[[0]*n for i in range(n)]
b=[[0]*n for i in range(n)]
c=[[0]*n for i in range(n)]
for i in range(m1):
    x,y,w=map(int,input().split())
    a[x][y]=w
for i in range(m2):
    x,y,w=map(int,input().split())
    b[x][y]=w
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]
for i in range(n):
    for j in range(n):
        if c[i][j]:
            print(i,j,c[i][j])
