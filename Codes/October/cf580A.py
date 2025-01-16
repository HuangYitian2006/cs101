n = int(input())
a = list(map(int, input().split()))
s, m = 1, 0
for i in range(len(a) - 1):
    if a[i] <= a[i + 1]:
        s += 1
    else:
        m = max(m, s)
        s = 1
m = max(m, s)
print(m)
