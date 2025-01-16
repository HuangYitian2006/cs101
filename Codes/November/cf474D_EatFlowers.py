t, k = map(int, input().split())
mod=1e9+7
a = [1 for i in range(100005)]
for i in range(1, k):
    a[i] = 1
for i in range(k, 100002):
    a[i]=a[i-1]+a[i-k]
    a[i] %= (1e9 + 7)
s = [0 for i in range(100005)]
for i in range(1, 100003):
    s[i] = s[i - 1] + a[i]
for i in range(t):
    l, r = map(int, input().split())
    print(int((s[r] - s[l - 1])%mod))
