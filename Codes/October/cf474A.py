kb = 'qwertyuiopasdfghjkl;zxcvbnm,./'
m = input()
a = input()
if m == 'R':
    for i in range(len(a)):
        print(kb[kb.index(a[i]) - 1],end='')
else:
    for i in range(len(a)):
        print(kb[kb.index(a[i]) + 1],end='')
