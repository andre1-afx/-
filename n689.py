from collections import deque, defaultdict

N, M, K = map(int, input().split())
books = list(map(int, input().split()))

graph = defaultdict(list)
in_degree = [0] * N

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

# 技能書裡的技能直接解鎖
unlocked = set(books)
queue = deque(books)

while queue:
    node = queue.popleft()
    for nei in graph[node]:
        in_degree[nei] -= 1                          # 減鄰居的入度
        if in_degree[nei] == 0 and nei not in unlocked:  # 入度歸零且還沒解鎖
            unlocked.add(nei)
            queue.append(nei)

print(len(unlocked))