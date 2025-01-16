n=int(input())
a=list(map(int,input().split()))
dp1=[1 for i in range(n)] # 增加
dp2=[1 for i in range(n)] # 减小
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp1[i]=max(dp1[i],dp2[j]+1)
        elif a[i]<a[j]:
            dp2[i]=max(dp2[i],dp1[j]+1)
m=0
for i in range(n):
    m=max(m,dp1[i],dp2[i])
print(m)