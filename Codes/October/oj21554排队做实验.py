n=int(input())
a=list(map(int,input().split()))
v=[(a[i],i)for i in range(len(a))]
v.sort(key=lambda hyt:hyt[0])
ans=[]
s=0.0
for i in range(len(a)):
    ans.append(v[i][1]+1)
    s+=v[i][0]*(n-i-1)
print(*ans)
print(f'{s/n:.2f}')