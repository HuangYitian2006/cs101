n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
b.sort()
i,j,s=0,0,0
while i<n and j<m:
    if abs(a[i]-b[j])<=1:
        s+=1
        i+=1
        j+=1
    elif a[i]>b[j]:
        j+=1
    else:
        i+=1
print(s)