n=int(input())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
if sorted(a,key=lambda f:f[0])==sorted(a,key=lambda f:f[1]):
    print('Poor Alex')
else:
    print('Happy Alex')