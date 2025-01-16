y = 'aeiouyAEIOUY'
a = input()
ans = ''
for i in range(len(a)):
    if a[i] in y:
        continue
    if 'A' <= a[i] <= 'Z':
        ans += '.' + chr(ord(a[i]) + 32)
    else:
        ans += '.' + a[i]
print(ans)
