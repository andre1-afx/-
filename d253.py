import sys
for line in sys.stdin:
    n = int(line)
    coin = [1, 5, 10, 25, 50]
    dp = [[0] * (n + 1) for _ in range(6)]          # 2. 6 列 × (n+1) 格
    dp[0][0] = 1
    for i in range(1, 6):
        dp[i][0] = 1
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]                  # 不用第 i 種硬幣
            if j >= coin[i - 1]:                     # 1、3. 只看第 i 種硬幣
                dp[i][j] += dp[i][j - coin[i - 1]]   # 用第 i 種，再看同一列
    print(dp[5][n])