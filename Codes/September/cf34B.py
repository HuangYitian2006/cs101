n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
s=0
for i in range(len(a)):
    if a[i]<0:
        b.append(-a[i])
if len(b)<=m:
    print(sum(b))
else:
    b.sort(reverse=True)
    for i in range(m):
        s+=b[i]
    print(s)