def y(n, m):
    if n == 1:
        return 1
    else:
        return (y(n - 1, m) + m-1) % n+1


while True:
    n, m = map(int, input().split())
    if {n, m} == {0}:
        break
    print(y(n, m))
