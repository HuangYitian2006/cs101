n,m=map(int,input().split())
ans=float('inf')
store_prices = [input().split() for _ in range(n)]
coupons = [input().split() for _ in range(m)]
def dfs(item=0,tot=0,each_store=[0]*m):
    global ans
    if item==n:
        discount=0
        for i in range(m):
            store_discount=0
            for coupon in coupons[i]:
                a,b=map(int,coupon.split('-'))
                if each_store[i]>=a:
                    store_discount=max(store_discount,b)
            discount+=store_discount
        ans=min(ans,tot-(tot//300)*50-discount)
        return
    for i in store_prices[item]:
        idx,p=map(int,i.split(':'))
        each_store[idx-1]+=p
        dfs(item+1,tot+p,each_store)
        each_store[idx-1]-=p



dfs()
print(ans)