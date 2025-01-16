import sys

n,t=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
if s<t:
    print(0)
    sys.exit()
dp=[0]*(s+1)
dp[0]=1
for i in range(n):
    for j in range(s,a[i]-1,-1):
        dp[j]=max(dp[j],dp[j-a[i]])
for i in range(t,s+1):
    if dp[i]:
        print(i)
        break