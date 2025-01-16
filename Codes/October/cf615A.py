n, m = map(int, input().split())
s = [0 for _ in range(m)]
for i in range(n):
    a = list(map(int, input().split()))
    for i in range(1, len(a)):
        s[a[i] - 1] = 1
print(['YES', 'NO'][0 in s])
