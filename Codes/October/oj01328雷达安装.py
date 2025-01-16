import math

j = 0
while True:
    j += 1
    n, d = map(int, input().split())
    if n == d == 0:
        break
    a, s, x = [], 0, -float('inf')
    mk = 0
    for i in range(n):
        x1, y1 = map(int, input().split())
        a.append((x1, y1))
        if y1 > d:
            mk = 1
    input()
    if mk:
        print(f'Case {j}: -1')
        continue
    a.sort(key=lambda f: f[0])
    b=[]
    for i in range(n):
        b.append((a[i][0]-math.sqrt(d**2-a[i][1]**2),
                  a[i][0]+math.sqrt(d**2-a[i][1]**2)))
    b.sort(key=lambda f: f[1]) #按右端点排
    for i in range(n):
        if x<b[i][0]:
            x=b[i][1]
            s+=1
    print(f'Case {j}: {s}')
