c={'+','-','*','/'}
def cal(s):
    if len(s)==1:
        return float(s[0])
    x1,x2,s1,s2=0,0,0,0
    for i in range(1,len(s)):
        if s[i] in c:
            s1+=1
        else:
            s2+=1
        if s2-s1==1:
            x1=i
            break
    if s[0]=='+':
        return cal(s[1:x1+1])+cal(s[x1+1:])
    if s[0] == '-':
        return cal(s[1:x1 + 1]) - cal(s[x1 + 1:])
    if s[0] == '*':
        return cal(s[1:x1 + 1]) * cal(s[x1 + 1:])
    if s[0] == '/':
        return cal(s[1:x1 + 1]) / cal(s[x1 + 1:])


a=list(input().split())
print(f'{cal(a):.6f}')