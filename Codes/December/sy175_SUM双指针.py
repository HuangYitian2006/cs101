n,s=map(int,input().split())
ans=0
a=list(map(int,input().split()))
l,r=0,n-1
while l<r:
    h=a[l]+a[r]
    if h==s:
        ans+=1
        l,r=l+1,r-1
    elif h>s:
        r-=1
    else:
        l+=1
print(ans)