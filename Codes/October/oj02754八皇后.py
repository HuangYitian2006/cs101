ans = []
s = ''


def f(n):
    global s
    if n == 9:
        ans.append(s)
        return
    for c in range(1, 9):
        for j in range(len(s)):
            if c == int(s[j]) or abs(c - int(s[j])) == abs(j - len(s)):
                break
        else:
            s += str(c)
            f(n + 1)
            s = s[:-1]


n = int(input())
f(1)
for i in range(n):
    print(ans[int(input()) - 1])
