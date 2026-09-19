N,M=map(int,input().split())
heights=[0]+list(map(int,input().split()))


path=[[] for j in range(N+1)]
order=sorted(range(1,N+1),key=lambda i : heights[i])
target=[]
for _ in range(M):
    u,v=map(int,input().split())
    if heights[u]<heights[v]:
        path[u].append(v)
    else:
        path[v].append(u)

    
Q=int(input())
for _ in range(Q):
    line=list(map(int,input().split()))
    target=line[1:]
    demand=set(target)
    dp=[(-1,-1)]*len(heights)
    for u in order:
        if u in demand:
            dp[u]=max((1,1),dp[u])
        else:
            dp[u]=max((0,1),dp[u])
        for v in path[u]:
            if v in demand:
                candiate=(dp[u][0]+1,dp[u][1]+1)
            else :
                candiate=(dp[u][0]+0,dp[u][1]+1)
            dp[v]=max(dp[v],candiate)
    t,x=max(dp)
    print(t,x)