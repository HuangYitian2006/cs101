n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
s0=sum(a)
s=0
for i in range(len(a)):
    s+=a[i]
    if 2*s>s0:
        break
print(i+1)