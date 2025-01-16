dy=[0,1,0,-1]
dx=[-1,0,1,0]
n,m=map(int,input().split())
a=[]
mx=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        s=0
        s+=1000*a[0][j]+100*a[i][m-1]+10*a[n-1][j]+a[i][0]
        s*=a[i][j]
        mx=max(mx,s)
print(mx)