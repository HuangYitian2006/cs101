while True:
    a,b=map(int,input().split())
    if a<b:
        a,b=b,a
    if a==b==0:
        break
    flag=0
    while True:
        flag+=1
        if a//b>=2 or a==b:
            print('win' if flag%2 else'lose')
            break
        else:
            a,b=b,a%b
