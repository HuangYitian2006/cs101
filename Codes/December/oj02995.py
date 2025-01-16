n=int(input())
a=list(map(int,input().split()))
dp1=[1 for i in range(n)]
dp2=[1 for i in range(n)]
dp1[0],dp2[0]=1,1
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp1[i]=max(dp1[i],dp1[j]+1)
        elif a[i]<a[j]:
            dp2[i]=max(dp2[i],dp2[j]+1,dp1[j]+1)
        #print(dp1,dp2)
print(max(max(dp1),max(dp2)))