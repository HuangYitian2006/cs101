n=int(input())
s=0
for i in range(n):
    a=input().split()
    mk=1
    for j in a:
        if j[0]=='#' and mk:
            s+=1
            mk=0
        elif j[0]!='#':
            mk=1
print(s)