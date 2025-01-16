n=int(input())
a=[0 for i in range(1200)]
# 4 7 44 47 74 77 4__ 7__
lk=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
for i in lk:
    j=1
    while i*j<1200:
        a[i*j]=1
        j+=1
print(['NO','YES'][a[n]])
