from collections import deque

while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    a=deque()
    ans=[]
    for i in range(1,n+1):
        a.appendleft(i)
    a.rotate(p-1)
    """for i in range(p-1):
        a.append(a.popleft())"""
    while a:
        """for i in range(m-1):
            a.append(a.popleft())"""
        a.rotate(m-1)
        ans.append(str(a.pop()))
    print(','.join(ans))