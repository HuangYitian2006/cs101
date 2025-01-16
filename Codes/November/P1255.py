a=int(input())
dp=[0 for i in range(6000)]
dp[0],dp[1]=1,2
for i in range(2,a):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[a-1])