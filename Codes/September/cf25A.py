import math

n=int(input())
a=list(map(int,input().split()))
t=0
for i in range(n):
    t+=a[i]%2
x=0
if t==1:
    for i in range(n):
        if a[i]%2==1:
            x=i+1
else:
    for i in range(n):
        if a[i]%2==0:
            x=i+1
print(x)