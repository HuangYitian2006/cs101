n,m=map(int,input().split())
a=[[0]for i in range(n+1)]
a[0]+=[0]*m
a+=[[0]*(m+1)]

for i in range(n):
    a[i+1]+=list(map(int,input().split()))
for i in range(n+2):
    a[i]+=[0]
#print(a)
s=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]:
            s+=4-a[i-1][j]-a[i+1][j]-a[i][j-1]-a[i][j+1]
print(s)