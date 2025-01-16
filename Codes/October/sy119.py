pole = 'ABC'


def hn(a, x, y):
    global pole
    if a == 1:
        print(f'{pole[x]}->{pole[y]}')
    else:
        hn(a - 1, x, 3 - x - y)
        print(f'{pole[x]}->{pole[y]}')
        hn(a - 1, 3 - x - y, y)


n = int(input())
print(2 ** n - 1)
hn(n, 0, 2)
