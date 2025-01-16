import math

while True:
    a1,a2,a3,a4,a5,a6=map(int,input().split())
    s=0
    if a1==a2==a3==a4==a5==a6==0:
        break
    s=s+a4+a5+a6
    s+=math.ceil(a3/4.0)
    a2-=a4*5
    a1-=a5*11
    if a3%4==1:
        a2-=5
        a1-=7
    elif a3%4==2:
        a2-=3
        a1-=6
    elif a3%4==3:
        a2-=1
        a1-=5
    if a2>=0 and a1>=0:
        s+=math.ceil((a1+4*a2)/36.0)
    elif a2<0:
        a1-=-a2*4
        if a1>0:
            s+=math.ceil(a1/36.0)
    elif a2 >= 0 > a1:
        s+=math.ceil(a2/9.0)
    print(s)