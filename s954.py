import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    d = [int(data[idx + i]) for i in range(N)]; idx += N
    M = int(data[idx]); idx += 1
    L = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1

    # 前綴和
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + d[i]

    # ws[i] = 從第 i 場開始播放 L 場能避免的傷害
    ws = [0] * N
    for i in range(N):
        ws[i] = prefix[min(i + L, N)] - prefix[i]

    # j=1: 只播一次，最佳就是 max(ws)
    ans = max(ws)
    prev = ws[:]  # prev[i] = dp[1][i]

    gap = L + C  # 兩次播放起點的最小間距

    for j in range(2, M + 1):
        # 建立 prev 的前綴最大值
        pmax = prev[:]
        for i in range(1, N):
            if pmax[i] < pmax[i - 1]:
                pmax[i] = pmax[i - 1]

        curr = [-1] * N  # -1 代表不合法
        best = -1
        for i in range(gap, N):
            p = i - gap
            if pmax[p] >= 0:
                val = pmax[p] + ws[i]
                curr[i] = val
                if val > best:
                    best = val

        if best > ans:
            ans = best
        prev = curr

    print(ans)

solve()

        


