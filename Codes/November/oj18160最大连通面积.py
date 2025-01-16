area=0
d=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def dfs(x,y):
    global area
    if a[x][y]=='.':
        return
    a[x][y]='.'
    area+=1
    for i in range(8):
        dfs(x+d[i][0],y+d[i][1])


for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[['.'for i in range(m+2)]for j in range(n+2)]#已经加了保护圈
    for i in range(1,n+1):# 这里使用了列表的切片赋值方法！
        a[i][1:m+1]=input()
    mx=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i][j]=='W':
                area=0
                dfs(i,j)
                mx=max(area,mx)
    print(mx)







