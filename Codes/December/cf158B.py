import math

n=int(input())
a=list(map(int,input().split()))
h=[0,0,0,0,0]
ans=0
for i in a:
    h[i]+=1
ans+=h[4]+h[3]+math.ceil(h[2]/2)
h[1]-=h[3]
if h[2]%2==1:
    h[1]-=2
if h[1]>0:
    ans+=math.ceil(h[1]/4)
print(ans)