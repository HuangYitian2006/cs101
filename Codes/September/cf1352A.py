n=int(input())
for i in range(n):
    s=0
    res=[]
    a=int(input())
    if a//10000>0:
        s+=1
        res.append(a//10000*10000)
    a%=10000
    if a//1000>0:
        s+=1
        res.append(a // 1000 * 1000)
    a%=1000
    if a//100>0:
        s+=1
        res.append(a // 100 * 100)
    a%=100
    if a // 10 > 0:
        s += 1
        res.append(a // 10 * 10)
    a %= 10
    if a // 1 > 0:
        s += 1
        res.append(a // 1 * 1)
    print(s)
    print(*res)