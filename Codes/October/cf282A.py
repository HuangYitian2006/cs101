n = int(input())
x = 0
for _ in range(n):
    a = input()
    x += [1, -1]['-' in a]
print(x)
