s=0
while True:
    s+=1
    a,b,c,n=map(int,input().split())
    if a==b==c==n==-1:
        break
    for i in range(n+1,30000):
        if (i-a)%23==(i-b)%28==(i-c)%33==0:
            print(f'Case {s}: the next triple peak occurs in {i-n} days.')
            break
