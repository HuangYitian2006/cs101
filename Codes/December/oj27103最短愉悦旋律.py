n,m=map(int,input().split())
a=list(map(int,input().split()))
s=set()
ans=0
for i in a:
    s.add(i)
    if len(s)==m:
        ans+=1
        s.clear()
print(ans+1)