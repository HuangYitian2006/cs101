n=int(input())
sx=sy=sz=0
for _ in range(n):
    x,y,z=map(int,input().split())
    sx+=x
    sy+=y
    sz+=z
print(['NO','YES'][sx==sy==sz==0])