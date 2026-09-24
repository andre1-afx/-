import sys
from collections import deque
data=sys.stdin.buffer.read().split()
N, M ,K,Q= int(data[0]), int(data[1]),int(data[2]), int(data[3])
adj = [[0] * N for _ in range(N)]
isaffected=[0]*N #病毒編號>裡面的編號就會被感染並改寫成病毒編號
for i in range(4,2*M+3,2):
    u,v=int(data[i]),int(data[i+1])
    adj[u][v]=1
    adj[v][u]=1
def pandemic(a,b,people,round,K):
    isaffected[a]=b
    new_patent=deque()
    new_patent.append(a)
    count=people
    curr=deque()
    
    while  round<K:
            
            while new_patent:
                u=new_patent.popleft()
                
                for l in range(N):
                    if adj[u][l]==1 and b>isaffected[l]:
                        isaffected[l]=b
                        curr.append(l)
            count+=len(curr)
            
            new_patent=curr.copy()
            curr.clear()
            round+=1
    return count
for i in range(2*M+4,(2*M+4)+2*Q,2):
    a,b=int(data[i]),int(data[i+1])
    
    print(pandemic(a,b,1,1,K))