import math

s,mx=0,0
n=int(input())
a=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    a[i][0:n]=map(int,input().split())
for i in range(n//2):
    s=0
    s+=sum(a[i][i:n-i])+sum(a[n-i-1][i:n-i])
    for j in range(i+1,n-i-1):
        s+=a[j][i]+a[j][n-i-1]
    mx=max(mx,s)
if n%2:
    mx=max(mx,a[n//2][n//2])
print(mx)