n=int(input())
a=list(map(int,input().split()))
s=int(input())
num=0
a.sort()
i,j=0,n-1
while i<j:
    if a[i]+a[j]==s:
        num+=1
        i+=1
        j-=1
    elif a[i]+a[j]>s:
        j-=1
    else:
        i+=1
print(num)