from collections import deque

N, M = map(int, input().split())

# 建鄰接表（雙向）
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

line = list(map(int, input().split()))
A = line[0]
initial = line[1:A+1]

# 多源 BFS
visited = set(initial)
queue = deque(initial)
days = 0

while queue:
    # 如果所有人都感染了就結束
    if len(visited) == N:
        break
    
    # 一次處理「這一天」的所有節點
    for _ in range(len(queue)):
        u = queue.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    
    days += 1

print(days)