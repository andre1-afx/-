import sys
input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())
    experiences = [list(map(int, input().split())) for _ in range(m)]

    NEG_INF = float('-inf')
    # dp[j][0/1/2]: 0=從左邊來, 1=剛進入這一列(從上面來/起點), 2=從右邊來
    dp = [[NEG_INF, NEG_INF, NEG_INF] for _ in range(n)]

    for i in range(m):
        prev = dp
        cur = [[NEG_INF, NEG_INF, NEG_INF] for _ in range(n)]

        # 1. 先算 k=1（剛進入這一列）
        for j in range(n):
            if i == 0:
                cur[j][1] = experiences[i][j]          # 第一列可任意起點
            else:
                best_prev = max(prev[j][0], prev[j][1], prev[j][2])
                if best_prev != NEG_INF:
                    cur[j][1] = best_prev + experiences[i][j]

        # 2. 左到右掃描，算 k=0（從左邊延伸過來）
        for j in range(1, n):
            left_best = max(cur[j-1][0], cur[j-1][1])
            if left_best != NEG_INF:
                cur[j][0] = left_best + experiences[i][j]

        # 3. 右到左掃描，算 k=2（從右邊延伸過來）
        for j in range(n - 2, -1, -1):
            right_best = max(cur[j+1][2], cur[j+1][1])
            if right_best != NEG_INF:
                cur[j][2] = right_best + experiences[i][j]

        dp = cur

    ans = max(max(row) for row in dp)
    print(ans)

solve()
      

    
