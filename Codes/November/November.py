import math		# AC时间: 202ms

n = int(input())
# 计算立方值并存储在列表中以避免重复计算
cubes = [i ** 3 for i in range(n + 1)]
ans = []
for b in range(2, n):
    for c in range(b, n):
        for d in range(c, n):
            if (a := cubes[b] + cubes[c] + cubes[d]) in cubes:
                ans.append((round(math.pow(a, 1 / 3)), b, c, d))
ans.sort()
for a, b, c, d in ans:
    print(f"Cube = {a}, Triple = ({b},{c},{d})")