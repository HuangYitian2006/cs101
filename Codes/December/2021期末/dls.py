n=0
v=[0]*105
def dfs(a,step):
    global n,x
    print(a,end=' ')
    v[a] = 1
    if step==x:
        return
    for i in range(n):
        if c[a][i] and v[i]==0:
            dfs(i,step+1)

n,m,x=map(int,input().split())
c=[[0]*n for i in range(n)]
for i in range(m):
    a1,a2=map(int,input().split())
    c[a1][a2]=c[a2][a1]=1
st=int(input())
dfs(st,0)