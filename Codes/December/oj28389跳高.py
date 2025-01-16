import bisect

n=int(input())
a=list(map(int,input().split()))
a.reverse()
dp=[10005]*100005
for i in range(n):
    dp[bisect.bisect_left(dp,a[i])]=a[i]
print(bisect.bisect_left(dp,10005))