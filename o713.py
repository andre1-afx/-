def ANS(sr,sc,maze):
    visited,distance,queue={(sr,sc)},defaultdict(list),deque([(sr,sc,0)])#初始走訪過、距離、BFS queue
    while queue:#計算距離
        sr,sc,r=queue.popleft()
        visited.add((sr,sc))
        distance[r].append((sr,sc))#以DISTANCE(0)做起點,裝走r步可以到的格子索引
        for cr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=sr+cr,sc+cc
            if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited and maze[nr][nc]>-1:
                visited.add((nr,nc))#+方向後走到的點
                queue.append((nr,nc,r+1))#走道的點+對應半徑
    visited={(sr,sc):0}#初始化引爆該格炸彈曾經的最大半徑
    for ans in range(1,max(distance)+1):#窮舉答案
        bomb=deque(distance[ans])#取出達到測試半徑可以多引爆的炸彈,這裡很重要,因為這樣每一次只需要處理distance[1],distance[2]以此類推
        while bomb:#每個點查看
            queue=deque()
            sr,sc=bomb.popleft()
            queue.append((sr,sc,maze[sr][sc]))
            while queue:#BFS
                sr,sc,r=queue.popleft()
                if ((sr,sc) not in visited or visited[(sr,sc)]<r) and r>=0:
                    visited[(sr,sc)]=r#記錄引爆該格最大半徑
                    if r>0:
                        for cr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr,nc=sr+cr,sc+cc
                            if 0<=nr<row and 0<=nc<col and maze[nr][nc]>-1:
                                queue.append((nr,nc,r-1))
                                if maze[nr][nc]>0:bomb.append((nr,nc))#半徑>=，1可以繼續連鎖反應
        if len(visited)>=q:return ans#引爆q個,visited本身是引爆了幾個
from collections import deque,defaultdict
row,col,q=map(int,input().split())
maze=[]
for r in range(row):
    line=list(map(int,input().split()))
    if -2 in set(line):sr,sc=r,line.index(-2)
    maze.append(line)
print(ANS(sr,sc,maze))

        