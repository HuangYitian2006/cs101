a=list(map(int,input().split()))
s=sum(a)
for i in range(4):
    if a[i]*3!=s:
        print(int(s/3-a[i]),end=' ')