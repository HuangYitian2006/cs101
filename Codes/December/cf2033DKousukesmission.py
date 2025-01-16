for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    s[0]=0
    dp=[0]*(n+1)
    for i in range(1,n+1):
        s[i]=s[i-1]+a[i-1] #i之前总和
    for i in range(n):
        dp[i+1]=dp[i]
        for j in range(0,i+1):
            if s[i+1]-s[j]==0:
                dp[i+1]=max(dp[i+1],dp[j]+1)

    #print(dp)
    print(max(dp))
