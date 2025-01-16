n,b=map(int,input().split())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
dp=[[0]*(b+1) for i in range(n)]
for i in range(n):
    for j in range(w[i],b+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+p[i])
print(dp[n-1][b])