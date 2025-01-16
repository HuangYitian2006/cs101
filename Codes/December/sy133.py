ans=[]
def dfs(x):
    global n
    if x>n:
        print(*ans)
        return
    for i in range(n):
        if used[i]==0:
            ans.append(a[i])
            used[i]=1
            dfs(x+1)
            used[i]=0
            ans.pop()

n=int(input())
a=list(map(int,input().split()))
a.sort()
used=[0]*n
dfs(1)