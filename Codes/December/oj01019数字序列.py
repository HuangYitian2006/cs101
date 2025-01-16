import bisect

s,l,ls='',[],0
for i in range(1,35000):
    s+=str(i)
    ls+=len(s)
    l.append(ls)
#print(s[0:100])
for i in range(int(input())):
    a=int(input())
    if a==1:
        print('1')
        continue
    x=bisect.bisect_right(l,a-1)
    #print(x,l[0:10])
    print(s[a-l[x-1]-1])

