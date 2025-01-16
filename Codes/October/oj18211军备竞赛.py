mn=int(input())
a=list(map(int,input().split()))
s1,s2,l,r=0,0,0,len(a)-1
a.sort()
while l<=r:
    if mn>=a[l]:
        s1+=1
        mn-=a[l]
        l+=1
    elif s1>s2 and mn+a[r]>=a[l] and l<r:
        s2+=1
        mn+=a[r]
        r-=1
    else:
        break
print(s1-s2)
