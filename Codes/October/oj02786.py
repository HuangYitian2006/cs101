dp=[0 for i in range(1000010)]
dp[1],dp[2]=1,2
for i in range(3,1000005):
    dp[i]=(2*dp[i-1]+dp[i-2])%32767
for i in range(int(input())):
    a=int(input())
    print(dp[a])