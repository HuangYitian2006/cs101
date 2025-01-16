t0,n=map(int,input().split())
t,w=[0]*n,[0]*n
dp=[0]*(t0+1)
for i in range(n):
    t[i],w[i]=map(int,input().split())
    #dp[t[i]]=max(dp[t[i]],w[i])
for i in range(n):
    for j in range(t0,t[i]-1,-1):
        if dp[j-t[i]] or j==t[i]:
            dp[j]=max(dp[j],dp[j-t[i]]+w[i])
#print(dp)
print(dp[t0] if dp[t0] else -1)
