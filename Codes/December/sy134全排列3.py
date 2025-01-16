from copy import deepcopy

ans=[]
cnt=[0]*9
def dfs(x):
    global n
    if x>n:
        print(*ans)
        return
    for i in range(n):
        if cnt[i]:
            ans.append(a[i])
            cnt[i]-=1
            dfs(x+1)
            cnt[i]+=1
            ans.pop()

n=int(input())
a=list(map(int,input().split()))
a.sort()
i=0
while i<n:
    j=i
    while j<n and a[j]==a[i]:
        cnt[i]+=1
        j+=1
    i=j
#print(cnt)
dfs(1)