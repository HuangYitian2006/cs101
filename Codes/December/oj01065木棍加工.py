for _ in range(int(input())):
    n=int(input())
    a0=list(map(int,input().split()))
    a=a0[0::2]
    b=a0[1::2]
    a=list(zip(b,a))
    a.sort()
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if a[i][1]<a[j][1]:
                dp[i]=max(dp[i],dp[j]+1)
    print(max(dp))