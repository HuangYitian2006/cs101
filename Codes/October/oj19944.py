n=int(input())
day=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for _ in range(n):
    a=input()
    c,y,m,d=int(a[0:2]),int(a[2:4]),int(a[4:6]),int(a[6:8])
    if m==1 or m==2:
        m+=12
        if y==0:
            y=99
            c-=1
        else:
            y-=1
    w=(y+y//4+c//4-2*c+int(26*(m+1)/10)+d-1)%7
    print(day[w])
