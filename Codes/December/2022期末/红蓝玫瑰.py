a=input()
n=len(a)
dp0,dp1=[0]*n,[0]*n
if a[0]=='R':
    dp1[0]=1
else:dp0[0]=1
for i in range(1,n):
    if a[i]=='R':
        dp0[i]=min(dp0[i-1],dp1[i-1]+1)
        dp1[i]=min(dp1[i-1]+1,dp0[i-1]+1)
    else:
        dp0[i]=min(dp0[i-1]+1,dp1[i-1]+1)
        dp1[i]=min(dp1[i-1],dp0[i-1]+1)
print(dp0[n-1])
