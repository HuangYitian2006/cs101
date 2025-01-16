import sys

n=int(input())
a=list(map(int,input().split()))
s0=sum(a)
if s0%3!=0:
    print(0)
    sys.exit()
s0=s0/3
l,r=0,n-1
sl,sr=0,0
dp=[0]*n
while r-l>=2:
    sl+=a[l]
    if sl==s0:
        dp[l]+=1
    dp[l]+=dp[l-1]
    l+=1
ans=0
while r>=2:
    sr+=a[r]
    if sr==s0:
        ans+=dp[r-2]
    r-=1
print(ans)