while True:
    try:
        x=input()
        a=set()
        for i in range(1, len(x) + 1):
            a.add(int(x[i-1:]+x[:i-1]))
        for i in range(1,len(x)+1):
            if int(x)*i not in a:
                print(x,'is not cyclic')
                break
        else: print(x,'is cyclic')
    except EOFError:
        break