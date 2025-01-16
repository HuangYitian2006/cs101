n=int(input())
a=input().split()
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]>a[j]+a[i]:
            a[i],a[j]=a[j],a[i]
rev=a[::-1]
print(''.join(rev),''.join(a))