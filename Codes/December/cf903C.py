n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
cnt=1
s=1
for i in range(1,n):
    if a[i]==a[i-1]:
        cnt+=1
        s = max(s, cnt)
    else:
        s=max(s,cnt)
        cnt=1
print(s)
