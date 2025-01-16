n,q=map(int,input().split())
like=[[0 for i in range(n+1)]for j in range(n+1)]
for i in range(q):
    a,b=map(int,input().split())
    like[a][b]=1
flag=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if like[i][j]==like[j][i]==1:
            flag=1
print('Yes' if flag else 'No')