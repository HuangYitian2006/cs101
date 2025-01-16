n=int(input())
s,e,w=[0]*n,[0]*n,[0]*n
for i in range(n):
    x,y,z=input().split()
    x1,y1=x.split('.'),y.split('.')
    s[i]=int(x1[1])-7+31*int(x1[0])-31
    e[i]=int(y1[1])-7+31*int(y1[0])-31
    w[i]=int(z)
dp=[0]*46
#print(s,e,w)
for i in range(0,45):
    dp[i]=dp[i-1]
    for j in range(n):
        if i==e[j]:
            dp[i]=max(dp[i],dp[s[j]-1]+w[j])

#print(dp)
print(max(dp))
'''2
1.8 1.10 100
1.10 1.15 200
5
1.8 1.27 100
1.10 1.19 90
1.23 1.27 20
2.4 2.8 81
2.10 2.21 100'''