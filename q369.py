from collections import deque

def BFS(grid, start, end, N, M):
    queue = deque([start])
    visited = {start}
    
    while queue:
        r, c = queue.popleft()
        
        if (r, c) == end:
            return True
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            if (0 <= nr < N and 0 <= nc < M
                and grid[nr][nc] != "#"
                and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc))
    
    return False


# 讀取輸入
N, M = map(int, input().split())

grid = []
for i in range(N):
    row = input()          # 每一行是一整條字串,不用 split()
    grid.append(row)

# 找出 S 和 T 的座標
start = None
target = None

for i in range(N):
    for j in range(M):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "T":
            target = (i, j)

# 執行 BFS 並輸出結果
if BFS(grid, start, target, N, M):
    print("mission passed respect+")
else:
    print("wasted")