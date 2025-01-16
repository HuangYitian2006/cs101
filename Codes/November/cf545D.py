n=int(input())
a=list(map(int,input().split()))
a.sort()
s=0
ans=0
for i in range(len(a)):
    if a[i]>=s:
        ans+=1
        s+=a[i]
print(ans)