import math

n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
m=math.ceil(n/2.0)-1
mx=-float('inf')
for i in range(m+1):
    s=0
    x,y=i,i
    while y<n-i-1:
        #print(x,y)
        s+=a[x][y]
        y+=1
    while x<n-i-1:
        #print(x,y)
        s+=a[x][y]
        x+=1
    #x-=1
    while y>i:
        #print(x,y)
        s+=a[x][y]
        y-=1
    #y+=1
    while x>i:
        #print(x,y)
        s+=a[x][y]
        x-=1
    #print(s)
    mx=max(mx,s)
mx=max(mx,a[m][m])
print(mx)