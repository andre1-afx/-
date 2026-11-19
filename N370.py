N, K = map(int, input().split())
chart = [0] * (N + 1)
for _ in range(K):
    start, end = map(int, input().split())
    chart[start] = end

MOD = 998244353
dp = [0] * (N + 1)
dp[N] = 1

for i in range(N - 1, 0, -1):
    total = 0
    for x in range(1, 7):
        nxt = min(i + x, N)
        if chart[nxt] > 0:
            nxt = chart[nxt]
        total += dp[nxt]
    dp[i] = total % MOD

print(dp[1])