a=int(input())
b=bin(a)[2:]
if b==b[::-1]:
    print('Yes')
else:
    print('No')