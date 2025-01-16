used=[0 for i in range(10)]
a=[]
def f(n):
    global x
    if n>x:
        print(*a)
        return
    for i in range(x):
        if used[i]==0:
            a.append(i+1)
            used[i]=1
            f(n+1)
            used[i]=0
            a.pop()




x=int(input())
f(1)