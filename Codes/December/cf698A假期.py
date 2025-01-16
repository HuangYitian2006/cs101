n=int(input())
a=list(map(int,input().split()))
dp=[[float('inf')]*3 for i in range(n)] #本日休息/锻炼/打比赛
dp[0][0]=1
if a[0]==1 or a[0]==3:
    dp[0][1]=0
if a[0]==2 or a[0]==3:
    dp[0][2]=0
for i in range(1,n):
    dp[i][0]=min(dp[i-1])+1
    if a[i]==1 or a[i]==3:
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])
    if a[i]==2 or a[i]==3:
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])
print(min(dp[n-1]))
