a=int(input())
x=bin(a)
if x[2:]==x[len(x)-1:1:-1]:
    print('Yes')
else:print('No')