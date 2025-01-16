n=int(input())
a=[]
l=100
for i in range(n):
   a.append(input())
   l=min(l,len(a[i]))
for i in range(l):
    flag=0
    for j in range(1,n):
        if a[j][i]!=a[j-1][i]:
            flag=1
            break
    if flag:
        print(a[0][:i])
        break
    elif i==l-1:
        print(a[0][:l])