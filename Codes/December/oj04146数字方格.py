n=int(input())
mx=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if (i+j)%2==0 and (j+k)%3==0 and (i+j+k)%5==0:
                mx=max(mx,i+j+k)
print(mx)