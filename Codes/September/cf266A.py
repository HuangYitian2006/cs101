n=input()
a=input()
s=0
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        s+=1
print(s)