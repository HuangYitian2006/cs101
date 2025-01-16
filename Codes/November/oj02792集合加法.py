from collections import Counter

for _ in range(int(input())):
    s=int(input())
    ax=int(input())
    a=list(map(int,input().split()))
    bx = int(input())
    b = list(map(int, input().split()))
    numa=[0 for i in range(1000005)]
    numb=[0 for i in range(1000005)]
    ans=0
    for i in range(ax):
        numa[a[i]]+=1
    for i in range(bx):
        numb[b[i]]+=1
    for i in range(ax):
        ans+=numb[s-a[i]]
    print(ans)


