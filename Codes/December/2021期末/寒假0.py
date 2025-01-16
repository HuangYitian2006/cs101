from functools import cmp_to_key

n=int(input())
s=[[0,0,0]for i in range(n)]
for i in range(n):
    x,y,z=input().split()
    x1,y1=x.split('.'),y.split('.')
    s[i][0]=int(x1[1])-7+31*int(x1[0])-31
    s[i][1]=int(y1[1])-7+31*int(y1[0])-31
    s[i][2]=int(z)
dp=[[0]*46 for i in range(n)]
s.sort(key=lambda x:x[1])
for i in range(n):
    for j in range(0,45):
        if j<s[i][1]:
            dp[i][j]=dp[i-1][j]
        else:
            if s[i][0]>0:
                dp[i][j]=max(dp[i-1][j],dp[i-1][s[i][0]-1]+s[i][2])
            else:
                dp[i][j]=max(dp[i-1][j],s[i][2])
#print(dp)
print(max(max(i) for i in dp))