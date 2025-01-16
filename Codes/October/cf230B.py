import math

'''
def check(m):
    if math.sqrt(m)%1 or m==1:
        return 'NO'
    for j in range(2,int(math.sqrt(math.sqrt(m)))+1):
        if math.sqrt(m)%j==0:
            return 'NO'
    return 'YES'
'''
def check(q):
    if math.sqrt(q)%1 or q==1:
        return 'NO'
    elif ans[int(math.sqrt(q))]:
        return 'YES'
    else:
        return 'NO'

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
    return prime


n = int(input())
a = list(map(int, input().split()))
pm=euler(10**6+10)
ans=[0 for i in range(10**6+10)]
for i in pm:
    ans[i]=1
pm2=[i**2 for i in pm]
for i in range(len(a)):
    print(check(a[i]))