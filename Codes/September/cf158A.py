n,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(0,len(a)):
    if i<k:
        if a[i]>0: s+=1
        else: break
    if i>=k:
        if a[i]==a[k-1]: s+=1
        else: break
print(s)