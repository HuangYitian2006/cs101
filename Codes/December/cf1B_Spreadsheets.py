import re

def a(s): #R23C55->BC23
    ans=''
    r,c=map(int,s[1:].split('C'))
    while c:
        ans=chr(65+(c-1)%26)+ans
        c=(c-1)//26
    ans+=str(r)
    return ans
def b(s): #BC23->R23C55
    pos=0
    while not s[pos].isdigit():
        pos+=1
    c=s[0:pos]
    c1=0
    i=1
    while i<=len(c):
        c1+=(ord(c[len(c)-i])-64)*(26**(i-1))
        #c1+=26**(i-1)
        i+=1
    return f'R{s[pos:]}C{c1}'
for _ in range(int(input())):
    ss=input().strip() #and s[len(s)//2]=='C' and 48<=ord(s[1])<=57
    if re.match(r'R\d+C\d+',ss):
        print(a(ss))
    else:
        print(b(ss))
