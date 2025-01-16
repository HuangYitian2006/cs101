n = int(input())
for i in range(n):
    a = int(input())
    v2 = v3 = 0
    a2 = a3 = a
    while not a2 % 2:
        v2 += 1
        a2 //= 2
    while not a3 % 3:
        v3 += 1
        a3 //= 3
    if v2 > v3 or a // (2 ** v2) // (3 ** v3) > 1:
        print('-1')
    else:
        print(2 * v3 - v2)
