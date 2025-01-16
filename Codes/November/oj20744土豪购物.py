a=list(map(int,input().split(',')))
dp1=[-float('inf') for i in range(len(a))]
dp2=[-float('inf') for i in range(len(a))]
s=[0 for i in range(len(a)+1)]
s[0]=0
for i in range(1,len(a)+1):
    s[i]=a[i-1]+s[i-1]
dp1[0]=a[0]
for i in range(len(a)):
    dp1[i]=max(a[i],dp1[i-1]+a[i])
    dp2[i]=max(dp1[i-1],dp2[i-1]+a[i])
print(max(max(dp1),max(dp2)))