a = '0' + input() +'0'
s=0
f=[0 for i in range(len(a)+1)]
for i in range(1,len(a)-1):
    if a[i] == a[i + 1]:
        s += 1
    f[i]=s
#print(f)
for i in range(int(input())):
    l, r = map(int, input().split())
    print(f[r-1] - f[l-1])
