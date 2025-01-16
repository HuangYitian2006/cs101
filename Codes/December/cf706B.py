n=int(input())
price=list(map(int,input().split()))
q=int(input())
dp=[0]*100005
price.sort()
for i in price:
    dp[i]+=1
for i in range(1,100005):
    dp[i]+=dp[i-1]
for i in range(q):
    x=int(input())
    if x>100004:
        print(dp[-1])
    else:
        print(dp[x])