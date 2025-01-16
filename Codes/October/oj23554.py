n=int(input())
m=[1 for _ in range(n)]
x=[]
a=list(map(int,input().split()))
for i in a:
    if i>n:
        x.append(i)
    else:
        m[i-1]=0
for i in range(n):
    if m[i]:
        print(i+1,end=' ')
print('\n',end='')
print(*sorted(x))