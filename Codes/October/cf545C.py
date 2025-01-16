n=int(input())
a=[]
s=0
for i in range(n):
    x1,h1=map(int,input().split())
    a.append((x1,h1))
a.sort(key=lambda f:f[0])
x=-float('inf')
x1=0
for i in range(n-1):
    l,m,r=a[i][0]-a[i][1],a[i][0],a[i][0]+a[i][1]
    if x<l:
        s+=1
        x=m
    elif l<=x<m and r<a[i+1][0]:
        s+=1
        x=r
    else:
        x=m

print(s+1)