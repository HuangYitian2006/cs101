from math import sqrt
def pfactors(n):
    """Finds the prime factors of 'n'"""

    pfact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pfact.append(check)
            num /= check
    if num > 1:
        pfact.append(num)
    return pfact

cnt=[0]*1000005
a=int(input())
p=pfactors(a)
s=0
flag=0
#print(p)
for i in p:
    if cnt[int(i)]==0:
        s+=1
    else:
        flag=1
    cnt[int(i)]+=1
if flag:
    print(0)
elif s%2==0:
    print(1)
else:
    print(-1)