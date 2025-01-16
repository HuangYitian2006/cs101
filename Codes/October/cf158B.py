import math

n = int(input())
a = list(map(int, input().split()))
s = [0, 0, 0, 0, 0]
t = 0
for i in range(len(a)):
    s[a[i]] += 1
t += s[4] + s[3]
s[1] -= s[3]
s[1] -= (s[2] % 2) * 2
t += math.ceil(s[2] / 2)
if s[1] > 0:
    t += math.ceil(s[1] / 4)
print(t)
