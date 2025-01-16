def euler(r):
    p=[0 for i in range(r+1)]
    prime=[]
    for i in range(2,r+1):
        if p[i]==0:
            prime.append(i)
        for j in prime:
            if i*j>r:
                break
            p[i*j]=1
            if i%j==0:
                break
    return p


n = int(input())
p=euler(10005)
ans=0
for i in range(2,n//2+1):
    if p[i]==p[n-i]==0:
        ans=i*(n-i)
print(ans)