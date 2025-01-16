n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
i=0
while i<n:
    if a[i]>sum(a[i:n])/k:
        k-=1
        i+=1
    else:
        print('%.3f'% (sum(a[i:n])/k))
        break
