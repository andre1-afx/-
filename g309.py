N,K=map(int,input().split())
roots=[0]*N#每個節點有幾個蛋糕
roots[0]=K  
subtrees=[[] for _ in range(N)]
for _ in range(N):
    a,L,R=map(int,input().split())
    subtrees[a].extend([L,R])
for j in range(N):
    validnode=1
    remain=roots[j]
    for x in subtrees[j]:
        if x==-1:

            continue
        else:
            validnode+=1
    for x in subtrees[j]:
        if x>0:
            roots[x]+=roots[j]//validnode
            remain-=roots[j]//validnode
    roots[j]=remain
print(*roots)
    

