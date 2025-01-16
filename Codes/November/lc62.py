m,n=map(int,input().split())
a=[[0 for i in range(n)]for j in range(m)]
for i in range(n):
    a[0][i]=1
for i in range(m):
    a[i][0]=1
for i in range(1,m):
    for j in range(1,n):
        a[i][j]=a[i-1][j]+a[i][j-1]
print(a[m-1][n-1])
