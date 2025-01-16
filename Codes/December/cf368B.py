n,m=map(int,input().split())
a=list(map(int,input().split()))
s=set()
dp=[0]*n
for i in range(n-1,-1,-1):
    if a[i] not in s:
        s.add(a[i])
    dp[i]=len(s)
for _ in range(m):
    print(dp[int(input())-1])