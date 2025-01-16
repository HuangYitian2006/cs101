def maxProfit(K, N, prices):
    if not prices or K == 0:
        return 0

    # 如果 K 大于 N/2，等价于不限交易次数
    if K >= N // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(N - 1))

    # 初始化 dp 数组
    dp = [[0] * N for _ in range(K + 1)]

    # 动态规划计算
    for k in range(1, K + 1):
        max_diff = -prices[0]  # 初始 max_diff
        for i in range(1, N):
            dp[k][i] = max(dp[k][i - 1], prices[i] + max_diff)
            max_diff = max(max_diff, dp[k - 1][i] - prices[i])

    return dp[K][N - 1]


# 输入和输出处理
T = int(input())  # 测试组数
for _ in range(T):
    K, N = map(int, input().split())
    prices = list(map(int, input().split()))
    print(maxProfit(K, N, prices))