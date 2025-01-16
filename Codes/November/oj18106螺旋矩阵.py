n = int(input())
s = n ** 2
a = [[0 for i in range(n)] for j in range(n)]
x = y = 0
vec = [[0, 1], [1, 0], [0, -1], [-1, 0]]
m = 0
while (s):
    a[x][y] = n ** 2 + 1 - s
    s-=1
    if 0 <= x + vec[m][0] <= n - 1 and 0 <= y + vec[m][1] <= n - 1:
        if a[x + vec[m][0]][y + vec[m][1]]==0:
            x += vec[m][0]
            y += vec[m][1]
        else:
            m += 1
            m %= 4
            x += vec[m][0]
            y += vec[m][1]
    else:
        m += 1
        m %= 4
        x += vec[m][0]
        y += vec[m][1]
for i in range(n):
    print(*a[i])