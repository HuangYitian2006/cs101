n,b=map(int,input().split())
*p,=map(int,input().split())
*w,=map(int,input().split())
#按照不同的重量来进行规划，引用上一个质量的结果
#同时第二个循环倒着走，就不会让一个东西被装多次了
dp=[0 for i in range(b+1)]
for i in range(n):
    for j in range(b,0,-1):
        if w[i]<=j:
            dp[j]=max(dp[j],dp[j-w[i]]+p[i])
print(dp[b])