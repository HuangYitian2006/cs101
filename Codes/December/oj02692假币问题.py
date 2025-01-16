def check(num,w):
    c=chr(ord('A')+num)
    for i in range(3):
        s=0
        for j in range(len(a[i][0])):
            if a[i][0][j]==c:
                s+=w
            elif a[i][1][j] == c:
                s-=w
        if ((s>0 and a[i][2]!='up') or (s==0 and a[i][2]!='even')
                or (s<0 and a[i][2]!='down')): #left heavy / even / left light
            return False
    return True


for _ in range(int(input())):
    a=[]
    for i in range(3):
        a.append(list(input().split()))
    f=0
    for i in range(12):
        if check(i,-1):
            print(chr(ord('A')+i),'is the counterfeit coin and it is light.')
        elif check(i,1):
            print(chr(ord('A') + i), 'is the counterfeit coin and it is heavy.')
