def check(s):
    if not ('@' in s and '.' in s):
        return 'NO'
    if s.count('@')!=1:
        return 'NO'
    if a[0] in {'@','.'} or a[len(a)-1] in {'@','.'}:
        return 'NO'
    if s.find('@.')!=-1 or s.find('.@')!=-1:
        return 'NO'
    q=s.find('@')
    if s.find('.',q)==-1:
        return 'NO'
    return 'YES'
while True:
    try:
        a = input()
    except EOFError:
        break
    print(check(a))

