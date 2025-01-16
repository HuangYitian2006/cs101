d=int(input())
n=int(input())
a=[[0 for i in range(1025)]for j in range(1025)]
for i in range(n):
    x,y,r=map(int,input().split())
    for j in range(max(0,x-d),min(1025,x+d+1)):
        for k in range(max(0,y-d),min(1025,y+d+1)):
            a[j][k]+=r
v,s=0,1
for i in range(1025):
    for j in range(1025):
        if v<a[i][j]:
            v=a[i][j]
            s=1
        elif v==a[i][j]:
            s+=1
print(s,v)