n = int(input())
a = 'I hate'
for i in range(0, n - 1):
    a += [' that I love', ' that I hate'][i % 2]
print(a + ' it')
