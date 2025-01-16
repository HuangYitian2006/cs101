for _ in range(int(input())):
    n=int(input())
    t=[]
    for i in range(n):
        l,r=map(int,input().split())
        t.append([l,r])
    t.sort(key=lambda f:f[1])
    ans,cur=0,-1
    for i in range(n):
        if cur<t[i][0]:
            ans+=1
            cur=t[i][1]
    print(ans)