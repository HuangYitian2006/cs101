a,m=[],[] #m栈用来装对应a某头猪以下的最小值
while True:
    try:
        s=input().split()
        if s[0]=='push':
            weight=int(s[1])
            a.append(weight)
            if m:
                m.append(min(m[-1],weight))
            else:
                m.append(weight)
        elif s[0]=='pop':
            if a:
                a.pop()
                m.pop()
        else:
            if a:
                print(m[-1])


    except EOFError:
        break