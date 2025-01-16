n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    mk = 0
    for i in [a, -a]:
        for j in [b, -b]:
            for k in [c, -c]:
                for l in [d, -d]:
                    if i + j + k + l == 24:
                        mk = 1
    print('YES' if mk else 'NO')
