#pylint:skip-file
from collections import deque
d=[(-1,0),(0,-1),(0,1),(1,0)]
def bfs(y1,x1,y2,x2):
    q=deque()
    q.append((0,y1,x1))
    inq=set()
    inq.add((y1,x1))
    while q:
        s,y,x=q.popleft()
        #print(s,y,x)
        if (y,x)==(y2,x2):
            return s
        for i in range(1,h+2):
            if 0<=y+i<=h+1:
                if a[y+i][x]=='X' and (y+i,x)!=(y2,x2):
                    break
                elif (a[y+i][x]==' ' or (y+i,x)==(y2,x2)) and (y+i,x) not in inq:
                    inq.add((y+i,x))
                    q.append((s+1,y+i,x))
        for i in range(-1,-h-2,-1):
            if 0<=y+i<=h+1:
                if a[y+i][x]=='X' and (y+i,x)!=(y2,x2):
                    break
                elif (a[y+i][x]==' ' or (y+i,x)==(y2,x2)) and (y+i,x) not in inq:
                    inq.add((y+i,x))
                    q.append((s+1,y+i,x))
        for i in range(1,w+2):
            if 0 <= x + i <= w + 1:
                if a[y][x+i]=='X' and (y,x+i)!=(y2,x2):
                    break
                if (a[y][x+i]==' ' or (y,x+i)==(y2,x2)) and (y,x+i) not in inq:
                    inq.add((y,x+i))
                    q.append((s+1,y,x+i))
        for i in range(-1,-w-2,-1):
            if 0 <= x + i <= w + 1:
                if a[y][x+i]=='X' and (y,x+i)!=(y2,x2):
                    break
                if (a[y][x+i]==' ' or (y,x+i)==(y2,x2)) and (y,x+i) not in inq:
                    inq.add((y,x+i))
                    q.append((s+1,y,x+i))

    return -1

i0=1
while True:
    w,h=map(int,input().split())
    if w==h==0:
        break
    print(f'Board #{i0}:')
    a=[[' ' for i in range(w+2)]for j in range(h+2)]
    for i in range(1,h+1):
        a[i][1:w+1]=input()
    # a[y][x]指向正确的位置
    j=1
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2==y1==y2==0:
            break
        s=bfs(y1,x1,y2,x2)
        if s==-1:
            print(f'Pair {j}: impossible.')
        else:
            print(f'Pair {j}: {s} segments.')
        j+=1
    print()
    i0+=1

