n=int(input())
l=input().split()
ans=[]
tmp=l[0]+' '
for i in l[1:]:
    if len(tmp)+len(i)>80:
        ans.append(tmp.rstrip())
        tmp=i+' '
    else:
        tmp+=i+' '
ans.append(tmp.rstrip())
print('\n'.join(ans))