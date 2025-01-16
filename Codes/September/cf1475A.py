n=int(input())
for i in range(n):
    a=int(input())
    while a!=1:
        if a%2==1:
            print('YES')
            break
        a//=2
    else:
        print('NO')