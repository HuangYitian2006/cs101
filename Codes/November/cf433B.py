n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
sa=[0 for i in range(n+1)]
sb=[0 for i in range(n+1)]
for i in range(1,n+1):
    sa[i]=sa[i-1]+a[i-1]
for i in range(1,n+1):
    sb[i]=sb[i-1]+b[i-1]
for _ in range(int(input())):
    t,l,r=map(int,input().split())
    if t==1:
        print(sa[r]-sa[l-1])
    if t==2:
        print(sb[r]-sb[l-1])
