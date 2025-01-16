n,m,n2,m2=map(int,input().split())
a,b=[],[]
c=[[0 for i in range(m-m2+1)] for j in range(n-n2+1)]
mx=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n2):
    b.append(list(map(int,input().split())))
for i in range(n-n2+1):
    for j in range(m-m2+1):
        s=0
        for i1 in range(n2):
            for j1 in range(m2):
                s+=b[i1][j1]*a[i+i1][j+j1]
        c[i][j]=s
for i in range(n-n2+1):
    print(*c[i])