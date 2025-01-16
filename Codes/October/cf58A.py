a = input()
b = 'hello_'
f = 0
for i in range(len(a)):
    if a[i] == b[f]:
        f += 1
if f == 5:
    print('YES')
else:
    print('NO')
