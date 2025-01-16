for _ in range(int(input())):
    l,n=map(int,input().split())
    *a,=map(int,input().split())
    m1,m2=-1,-1
    for i in range(n):
        m1=max(m1,min(l-a[i],a[i]))
        m2=max(m2,max(l-a[i],a[i]))
    print(m1,m2)