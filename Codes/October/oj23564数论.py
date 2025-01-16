import sys


def pFactors(n):
    """Finds the prime factors of 'n'"""
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(num)
    return pFact


n = int(input())
tmp = s = 0
if n == 1:
    print('1')
    sys.exit(0)
for i in pFactors(n):
    if i == tmp:
        print('0')
        break
    else:
        tmp = i
        s += 1
else:
    print('-1' if s % 2 else '1')
