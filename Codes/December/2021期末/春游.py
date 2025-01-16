n=int(input())
a=list(map(int,input().split()))
a.sort()
x=[0]*(n+1)
idx=0
for i in range(len(a)):
    if a[i]<=n:
        x[a[i]]=1
    else:
        idx=i
        break
for i in range(1,n+1):
    if x[i]==0:
        print(i,end=' ')
print()
print(*a[idx:])