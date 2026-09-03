N, M = map(int, input().split())
adj = [[] for _ in range(N)]
haveway = True

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 1. 度數檢查
for i in range(N):
    if len(adj[i]) >= 3:
        haveway = False
        break

# 2. 環檢查（DFS）
if haveway:
    visited = [False] * N
    for start in range(N):
        if visited[start]:
            continue
        # DFS with parent tracking
        stack = [(start, -1)]
        visited[start] = True
        while stack:
            u, parent = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, u))
                elif v != parent:
                    # 走到已訪問且不是父節點 → 環
                    haveway = False
                    break
            if not haveway:
                break

print("Yes" if haveway else "No")