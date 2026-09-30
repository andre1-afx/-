W, E, N = map(int, input().split())
dp = [0] * W          # dp[c]：花不超過 c 點血的最大傷害，c = 0..W-1

for _ in range(N):
    d, a = map(int, input().split())
    for c in range(W - 1, d - 1, -1):
        if dp[c - d] + a > dp[c]:
            dp[c] = dp[c - d] + a

for c in range(W):
    if dp[c] >= E:
        print(W - c)
        break
else:
    print("wryyyyyyyyyyyyy")