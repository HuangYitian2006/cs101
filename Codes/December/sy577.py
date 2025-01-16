a=input()
mx,cur=1,1
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        cur+=1
        mx=max(mx,cur)
    else:
        mx=max(mx,cur)
        cur=1
print(mx)