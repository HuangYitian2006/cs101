import heapq
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(sx,sy,tx,ty):
    global m,n,a
    if a[sx][sy]=='#' or a[tx][ty]=='#':
        return 'NO'
    heap=[(0,sx,sy)]
    power=[[float('inf') for i in range(n)] for j in range(m)]
    power[sx][sy]=0
    while heap:
        cpower,cx,cy=heapq.heappop(heap)#找到路径最短的点开始拓展！
        if cpower>power[cx][cy]: #已经更新了更好的到此处的方法，这一状态就不用了
            continue
        for i in range(4):
            nx,ny=cx+dx[i],cy+dy[i]
            if 0<=nx<m and 0<=ny<n and a[nx][ny]!='#':
                npower=cpower+abs(int(a[nx][ny])-int(a[cx][cy]))
                if npower<power[nx][ny]:
                    heapq.heappush(heap,(npower,nx,ny))
                    power[nx][ny]=npower
    if power[tx][ty]==float('inf'):
        return 'NO'
    else:
        return power[tx][ty]


m,n,p=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(input().split()))
for i in range(p):
    sx,sy,tx,ty=map(int,input().split())
    print(bfs(sx,sy,tx,ty))