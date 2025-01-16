n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort(key=lambda f:f[1],reverse=True)
cur,t=0,0
for i in range(n):
    cur+=a[i][0]
    t=max(t,cur+a[i][1])
print(t)