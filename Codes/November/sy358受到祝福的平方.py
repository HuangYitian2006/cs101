import math

a=input()
dp=[0 for i in range(len(a))]
for i in range(len(a)):
    for j in range(i+1):
        if math.sqrt(int(a[j:i+1]))%1==0 and int(a[j:i+1])!=0:
            if j>0:
                dp[i]=dp[i] or dp[j-1]
            if j==0:
                dp[i]=1
print('Yes' if dp[len(a)-1] else 'No')