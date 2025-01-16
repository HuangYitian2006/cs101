import math

t = int(input())
for _ in range(t):
    n = int(input())
    m = int(math.log2(n))
    print(int(n * (n + 1) / 2 - 2 * (2 ** (m + 1) - 1)))
