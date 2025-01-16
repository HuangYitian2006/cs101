n,m=map(int,input().split())
a=[0]+[int(x) for x in input().split()]+[m]
tot=0
for i in range(1,n+2,2):
    tot+=a[i]-a[i-1]
ans,s=tot,0
for i in range(2,n+2,2):
    s+=a[i-1]-a[i-2]
    if a[i]-a[i-1]>1:
        ans=max(ans,s+m-a[i-1]-(tot-s)-1)
print(ans)

