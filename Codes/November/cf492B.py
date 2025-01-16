n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
m=-float('inf')
for i in range(n-1):
    m=max(m,a[i+1]-a[i])
m=max(m,2*a[0],(l-a[n-1])*2)
print(m/2)