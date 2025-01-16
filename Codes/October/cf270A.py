n = int(input())
for _ in range(n):
    a = int(input())
    print('NO' if 360 % (180 - a) else 'YES')
