n = int(input())
nums = []

while len(nums) < n * n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i * n:(i + 1) * n])) for i in range(n)]
#print(matrix)
m=[[0]*(n+1) for i in range(n+1)]
s=[[0]*(n+1) for i in range(n+1)]
for i in range(n):
    m[i+1][1:n+1]=matrix[i]
for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+m[i][j]
mx=-float('inf')
for x1 in range(1,n+1):
    for y1 in range(1, n + 1):
        for x2 in range(x1, n + 1):
            for y2 in range(y1, n + 1):
                #s0=s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1]
                #print(x1,y1,x2,y2,s0)
                mx=max(mx,s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1])
#print(s[4][2]+s[1][0]-s[4][0]-s[1][2])
print(mx)

