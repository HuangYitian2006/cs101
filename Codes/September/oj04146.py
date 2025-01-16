n=int(input())
a=b=c=0
for a1 in range(1,n+1):
    for a2 in range(1,n+1):
        for a3 in range(1,n+1):
            if (a1+a2)%2==0 and (a2+a3)%3==0 and (a1+a2+a3)%5==0 and a1+a2+a3>a+b+c:
                a=a1
                b=a2
                c=a3
print(a+b+c)