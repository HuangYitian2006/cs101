from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(a,t):
    if a==t:
        return True
    if a<t or a%3!=0:
        return False
    return dfs(a/3,t) or dfs(a/3*2,t)
for _ in range(int(input())):
    a,t=map(int,input().split())
    print('YES' if dfs(a,t) else 'NO')
