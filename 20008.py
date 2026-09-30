H, E, S, W, N = 0, 1, 2, 3, 4
price = [None] + [list(map(int, input().split())) for _ in range(4)]  # price[E]..price[N]，順序剛好跟輸入一致
road = list(map(int, input().split()))

edges = [(H,E), (H,S), (H,W), (H,N), (E,S), (S,W), (W,N), (N,E)]
adj = [[] for _ in range(5)]
for i, (u, v) in enumerate(edges):
    adj[u].append((v, road[i]))
    adj[v].append((u, road[i]))
INF = float('inf')
travel = [INF] * 16

def dfs(node, mask, cost):
    if node == H:
        travel[mask] = min(travel[mask], cost)
    for nxt, w in adj[node]:
        if nxt == H:
            dfs(nxt, mask, cost + w)
        else:
            bit = 1 << (nxt - 1)
            if not (mask & bit):
                dfs(nxt, mask | bit, cost + w)

dfs(H, 0, 0)

ans = INF
for mask in range(1, 16):          # 空集合買不到東西，從 1 開始
    if travel[mask] == INF:
        continue
    goods = 0
    for k in range(4): 
        best=INF
        for m in range(1,5) :
            if mask & (1<<(m-1)):
                if price[m][k]<best:
                    best=price[m][k]
        goods+=best       # 馬、鞍、韉、鞭
        
    ans = min(ans, travel[mask] + goods)
print(ans)