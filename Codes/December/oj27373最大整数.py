from functools import cmp_to_key
def cmp(a,b):
    if a+b>b+a:
        return 1
    else:
        return -1

m=int(input())
n=int(input())
a=list(input().split())
dp=[['' for i in range(m+1)]for i in range(n+1)]
a.sort(reverse=True,key=cmp_to_key(cmp))
#print(a)
#dp[i] 前i个数最大结果
for i in range(1,n+1): #前i个数
    for j in range(1,m+1): #最多j位
        if len(dp[i-1][j-len(a[i-1])])+len(a[i-1])<=j:
            if dp[i-1][j]!='':
                dp[i][j]=str(max(int(dp[i-1][j-len(a[i-1])]+a[i-1]),int(dp[i-1][j])))
            else:
                dp[i][j]=dp[i-1][j-len(a[i-1])]+a[i-1]
        else:
            dp[i][j]=dp[i-1][j]
        #print(dp)
print(dp[n][m])