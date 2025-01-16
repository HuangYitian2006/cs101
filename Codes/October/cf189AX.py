n,a,b,c=map(int,input().split())
dp=[0]+[-float('inf') for i in range(10000)]
x=[a,b,c]
x.sort()
for i in range(x[0],n+1):
    dp[i]=max(dp[i-a],dp[i-b],dp[i-c])+1
print(dp[n])