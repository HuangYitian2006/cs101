n=int(input())
a,dp=[],[]
for i in range(n):
    a.append(list(map(int,input().split())))
    dp.append([0]*(i+1))
dp.append([0]*(n+1))
#print(a,dp)
for i in range(n-1,-1,-1):
    for j in range(i+1):
        dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+a[i][j]
print(dp[0][0])