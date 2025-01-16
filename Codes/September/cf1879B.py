t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    min_a=min(a)
    min_b=min(b)
    print(min(min_a*n+sum(b),min_b*n+sum(a)))