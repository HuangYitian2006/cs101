n,k,l,c,d,p,nl,np=map(int,input().split())
x=int(min(k*l/(nl*n),c*d/n,p/(np*n)))
print(x)