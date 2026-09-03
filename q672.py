N,M,K=map(int,input().split())
giantcity=list(map(int,input().split()))
parent=list(range(N+1))
rank=[0]*(N+1)
edges=[]
def find(x):
    if parent[x]!=x:
        
        parent[x]=find(parent[x])
    
        

    return parent[x]
def union(x,y):
    rx=find(x)
    ry=find(y)
    if rx==ry:
        return False
    if rank[rx]<rank[ry]:
        parent[rx]=ry
        
    elif rank[rx]>rank[ry]:
        parent[ry]=rx
        
    else :
        parent[ry]=rx
        rank[rx]+=1
    return True
def kruskal(edges):
    MST_cost=0
    for i in range(1,K):
        union(giantcity[0],giantcity[i])
    edges.sort(key=lambda x:x[2])
    for road in edges:
        if union(road[0],road[1]):
            MST_cost+=road[2]
        else :
            continue
    return MST_cost
for i in range(M):
    u,v,c=map(int,input().split())
    edges.append((u,v,c))
answer=kruskal(edges)
print(answer)