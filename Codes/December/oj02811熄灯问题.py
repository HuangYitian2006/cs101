import copy


def check(a,s):
    for i in range(1,7):
        if s[1][i]==1: #按下开关
            a[1][i] = 1 - a[1][i]
            a[1][i+1] = 1 - a[1][i+1]
            a[1][i-1] = 1 - a[1][i-1]
            a[1+1][i] = 1 - a[1+1][i]
            a[1-1][i] = 1 - a[1-1][i]
    for j in range(2,6):
        for i in range(1,7):
            if a[j-1][i]==1:#上方的亮就需要按开关，使上方一行熄灭
                s[j][i]=1
                a[j][i] = 1 - a[j][i]
                a[j][i + 1] = 1 - a[j][i + 1]
                a[j][i - 1] = 1 - a[j][i - 1]
                a[j + 1][i] = 1 - a[j + 1][i]
                a[j - 1][i] = 1 - a[j - 1][i]
    if a[5][1:7]==[0,0,0,0,0,0]:
        for i in range(1,6):
            print(*s[i][1:7])


b=[[0 for i in range(8)]for j in range(7)]
k=[[0 for i in range(8)]for j in range(7)]
for i in range(1,5+1):
    b[i][1:7]=map(int,input().split())
for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                for i5 in range(2):
                    for i6 in range(2):
                        k[1][1:7]=[i1,i2,i3,i4,i5,i6]
                        #print(k)
                        B=copy.deepcopy(b)
                        K=copy.deepcopy(k)
                        check(B,K)
