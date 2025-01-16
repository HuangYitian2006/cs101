h=2*float(input())
m=int(input())
ec=[[0,0]]*m
for i in range(m):
    ec[i]=list(map(float,input().split()))
h-=0.5*m
ec.sort(key=lambda f:f[0]*f[1],reverse=True)
index=0
ans=0
while h and index<m:
    if h<=5.0/ec[index][0]:
        ans+=h*ec[index][0]*ec[index][1]
        h=0
    else:
        ans+=5.0*ec[index][1]
        h-=5.0/ec[index][0]
        index+=1
print(f'{ans:.1f}')

