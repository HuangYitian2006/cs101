a=int(input())
dp=[0 for i in range(6000)]
dp[1]=1
for i in range(2,a+1):
    dp[i]=sum(dp)+1
print(dp[a])