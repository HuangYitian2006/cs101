n,a,b,c=map(int,input().split())
dp=[0 for i in range(5000)]
m=max(a,b,c)
for i in range(m):
    dp[i]=-1

for i in range(m,m+n):

    dp[i]=max(dp[i-a],dp[i-b],dp[i-c])+1
print(dp[m+n-1])