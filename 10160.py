import sys

data = sys.stdin.read().split()
idx = 0

def dfs(i, covered, count):
    global best
    # 1. 如果 covered == full：更新 best，return
    # 2. 如果 i == N：return
    # 3. 剪枝之後再加
    # 4. 在 i 蓋站：dfs(i + 1, covered | cover[i], count + 1)
    # 5. 不在 i 蓋站：dfs(i + 1, covered, count)
    if covered==full:
        if(count<best):
            best=count
        return
    if i==N:
        return
    if count>=best:
        return
    if covered | reach[i] != full:
        return


    
    if covered | cover[i] != covered:
        dfs(i + 1, covered | cover[i], count + 1)
    dfs(i + 1, covered, count)
while True:
    N = int(data[idx]); M = int(data[idx + 1])
    idx += 2
    if N == 0 and M == 0:
        break

    cover = [1 << i for i in range(N)]   # 第一步：每個城鎮先照顧自己

    for _ in range(M):
        a = int(data[idx]); b = int(data[idx + 1])
        idx += 2
        a -= 1; b -= 1
        cover[a] |= 1 << b               # 記錄 a 和 b 相連
        cover[b] |= 1 << a

    full = (1 << N) - 1                  # 第二步：全部照顧到的樣子
    best = N                             # 最差就是每個城鎮都蓋
    reach = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        reach[i] = reach[i + 1] | cover[i]
    dfs(0, 0, 0)                         # 從城鎮 0 開始，還沒照顧任何人，蓋了 0 站
    print(best)
