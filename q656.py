"""
Selling（賣蔬菜）— 單調佇列解法

dp[i] = 到達鄉鎮 i 的最大收益
dp[i] = max(dp[j], 其中 max(1, i-D) ≤ j ≤ i-1) + P[i]

用單調遞減佇列維護滑動窗口內 dp 的最大值，O(N) 解決。
"""

from collections import deque
import sys


def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1

    # P[1] = 0（起點不賣）, P[N] = 0（終點不賣）
    # 輸入的是 P[2], P[3], ..., P[N-1]
    P = [0] * (N + 1)
    for i in range(2, N):
        P[i] = int(data[idx]); idx += 1

    # dp[i] = 到達鄉鎮 i 的最大收益
    dp = [0] * (N + 1)

    # 單調遞減佇列，存索引，dp[前端] 永遠是窗口內最大
    dq = deque()
    dq.append(1)  # 起點 dp[1] = 0

    for i in range(2, N + 1):
        # ① 移除過期：索引 < i - D 的已經跳不到 i 了
        while dq and dq[0] < i - D:
            dq.popleft()

        # ② 轉移：從窗口內最大的 dp 值跳過來
        dp[i] = dp[dq[0]] + P[i]

        # ③ 維持單調：尾端 dp 值比 dp[i] 小的都淘汰
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()

        # ④ 加入新元素
        dq.append(i)

    print(dp[N])


solve()



        
    
