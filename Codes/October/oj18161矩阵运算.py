import sys

a1, a2 = map(int, input().split())
a = [[int(x) for x in input().split()] for i in range(a1)]
b1, b2 = map(int, input().split())
b = [[int(x) for x in input().split()] for i in range(b1)]
c1, c2 = map(int, input().split())
c = [[int(x) for x in input().split()] for i in range(c1)]
ans=[[0 for i in range(c2)]for j in range(c1)]
if not(a2==b1 and a1==c1 and b2==c2):
    print('Error!')
    sys.exit()
for i in range(c1):
    for j in range(c2):
        ans[i][j]+=c[i][j]
        s=0
        for k in range(a2):
            s+=a[i][k]*b[k][j]
        ans[i][j]+=s
for i in range(c1):
    print(*ans[i])