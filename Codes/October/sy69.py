def rn(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def add_day():
    global y, m, d
    mk=rn(y)
    d+=1
    if d>a[mk][m-1]:
        d=1
        m+=1
    if m>12:
        m=1
        y+=1

a = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

y, m, d = map(int, input().split('-'))
n = int(input())
for _ in range(n):
    add_day()
print(f'{y:04d}-{m:02d}-{d:02d}')
