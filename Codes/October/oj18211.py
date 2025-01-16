p=int(input())
a=list(map(int,input().split()))
s1,s2,l,r=0,0,0,len(a)-1
a.sort()
while l<=r:
    if p>=a[l]:
        s1+=1
        p-=a[l]
        l+=1
    elif s1>s2:
        p+=a[r]-a[l]
        l+=1
        r-=1
    else:break
print(s1-s2)