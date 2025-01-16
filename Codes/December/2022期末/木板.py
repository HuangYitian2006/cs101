h,l,n=map(int,input().split())
v=list(map(float,input().split()))
t=[]
for i in range(n):
    t.append(l/v[i])
t.sort()
t0=t[n//2-1 if n%2==0 else n//2]
#print(t0)
h0=h-5*t0**2
print(f'{h0:.2f}')