n,w=map(int,input().split())
s=0
a=[[0.0,0.0,0.0] for i in range(n)]
for i in range(n):
    a[i][0],a[i][1]=map(int,input().split())
    a[i][2]=a[i][0]/a[i][1]
a.sort(key=lambda f:f[2],reverse=True)
j=0
while w>0 and j<n:
    if w>a[j][1]:
        s+=a[j][0]
        w-=a[j][1]
    else:
        s+=w*a[j][2]
        break
    j+=1
print(f'{s:.1f}')
