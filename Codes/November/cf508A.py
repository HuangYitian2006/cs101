n,m,k=map(int,input().split())
a=[[0 for i in range(m+2)]for j in range(n+2)]
flag=0
for i in range(k):
    x,y=map(int,input().split())
    a[x][y]=1
    for j1 in (-1,1):
        for j2 in (-1,1):
            if a[x+j1][y]*a[x+j1][y+j2]*a[x][y+j2]:
                flag=1
    if flag:
        print(i+1)
        break
else:
    print(0)