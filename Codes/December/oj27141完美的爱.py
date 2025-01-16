n=int(input())
a=[int(x)-520 for x in input().split()]
s=0
p=dict()
ans=0
for i in range(n):
    s+=a[i]
    if s==0:
        ans=i+1
    elif s in p:
        ans=max(ans,i-p[s])
    else:
        p[s]=i
    #print(s,p,ans)
print(ans*520)
