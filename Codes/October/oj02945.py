n=int(input())
dp=[1 for i in range(n)]
h=list(map(int,input().split()))
for i in range(n):
    for j in range(i):
        if h[j]>=h[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))