n=int(input())
a=list(map(int,input().split()))
num=[0 for i in range(10**5+5)]
dp=[0 for i in range(10**5+5)]
for i in range(n):
    num[a[i]]+=1
for i in range(0,10**5+2):
    dp[i]=max(dp[i-1],dp[i-2]+i*num[i])
print(dp[100001])