while True:
    a=[]
    n=int(input())
    if n==0:
        break
    for i in range(n):
        a.append([int(i) for i in input().split()])
    a.sort()
  #  print(a)
    m,s=1000000,0
    for i in range(n):
        if a[i][1]<m:
            s+=1
            m=a[i][1]
    print(s)
