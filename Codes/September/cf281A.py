a=input()
b=''
for i in range(len(a)):
    if i==0:
        if ord(a[i])>=97:
            b+=chr(ord(a[i])-32)
        else:
            b+=a[i]
    else:
        b+=a[i]
print(b)