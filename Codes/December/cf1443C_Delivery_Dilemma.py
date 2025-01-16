ansx=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ab=list(zip(a,b))
    ab.sort(key=lambda f:(-f[0],f[1]))
    t=ab[0][0]
    i,s=0,0
    ans=t
    while i<n:
        if s+ab[i][1]<t:
            s+=ab[i][1]
            if i<n-1:
                t=ab[i+1][0]
                ans=max(t,s)
            else:
                ans=s
            i+=1
        else:break
    ansx.append(str(ans))
print('\n'.join(ansx))