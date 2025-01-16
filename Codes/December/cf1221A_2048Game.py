import math

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=[0]*32
    for i in range(n):
        m[int(math.log(a[i],2))]+=1
    for i in range(0,12):
        m[i+1]+=m[i]//2
    if m[11]:
        print('YES')
    else:
        print('NO')