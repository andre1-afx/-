import sys
from collections import deque
def bfs(grid, sr, sc):
    R, C = len(grid), len(grid[0])
    seen = [[False] * C for _ in range(R)]   # 標記走過
    q = deque([(sr, sc)])                     # 佇列，放起點
    seen[sr][sc] = True
    count = 0
    while q:                                  # 佇列還有東西
        r, c = q.popleft()                    # 拿最前面那格
        count += 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):   # 上下左右
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc] and grid[nr][nc] == '0':
                seen[nr][nc] = True           # 放進佇列時就標記
                q.append((nr, nc))            # 排到最後面
    return count
lines = sys.stdin.read().splitlines()
T = int(lines[0])

cases, cur = [], []
for line in lines[1:]:
    if line.strip() == "":
        if cur:
            cases.append(cur); cur = []
    else:
        cur.append(line.strip())
if cur:
    cases.append(cur)

answers = []
for case in cases:
    i, j = map(int, case[0].split())
    grid = case[1:]
    answers.append(str(bfs(grid, i - 1, j - 1)))
print("\n\n".join(answers))