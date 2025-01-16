n, m = map(int, input().split())
i=0
while n:
    i+=1
    if i%m==0:
        n+=1
    n-=1
print(i)