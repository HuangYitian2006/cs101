from collections import deque
def bfs(n):
    inq=set()
    inq.add(1)
    q=deque()
    q.append((0,1))
    while q:
        step,num=q.popleft()
        if num==n:
            return step
        if num+1<=n and num+1 not in inq:
            inq.add(num+1)
            q.append((step+1,num+1))
        if num*2<=n and num*2 not in inq:
            inq.add(num*2)
            q.append((step+1,num*2))

a=int(input())
print(bfs(a))