a=input()
a=a.lower()
s=1
for i in range(len(a)):
    if i==len(a)-1:
        print(f'({a[i]},{s})', end='')
    elif a[i]==a[i+1]:
        s+=1
    else:
        print(f'({a[i]},{s})',end='')
        s=1
