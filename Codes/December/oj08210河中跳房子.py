def check(x):
    num,now=0,0 #移除个数、当前保留位置
    for i in range(1,n+2):#把终点也放入，若终点不满足，则把上一个去掉！
        if d[i]-now<x:
            num+=1
        else:
            now=d[i]
    if num>m:
        return True
    else:
        return False

L,n,m=map(int,input().split())
d=[0]
a=[]
for i in range(n):
    d.append(int(input()))
d.append(L)
l,r=0,L+1
ans=0
while l<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else: #这个距离可以做到！
        ans=mid
        l=mid+1 #一定要+1，否则可能死循环！
print(ans)