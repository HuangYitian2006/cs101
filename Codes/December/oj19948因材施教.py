n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
a.sort()
for i in range(1,n):
    b.append(a[i]-a[i-1])
b.sort(reverse=True)
#print(b)
print(a[n-1]-a[0]-sum(b[0:m-1]))
