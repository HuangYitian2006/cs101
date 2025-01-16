import bisect

n=int(input())
price=list(map(int,input().split()))
price.sort()
q=int(input())
for i in range(q):
    x=int(input())
    print(bisect.bisect(price,x))