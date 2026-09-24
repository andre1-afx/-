coords=set()
N=int(input())
intervals=[]
for i in range(N):
    L,R=map(int,input().split())
    intervals.append((L,R))
    coords.add(L)
    coords.add(R+1)
coords=sorted(coords)
coords_map={v:i for i,v in enumerate(coords)}
diff=[0]*len(coords)
for L,R in intervals:
    idx_L=coords_map[L]
    idx_R=coords_map[R+1]
    diff[idx_L]+=1
    diff[idx_R]-=1
cover=0
max_cover=0
max_idx=0
for i in range(len(diff)):
    cover+=diff[i]
    if cover>=max_cover:
        max_cover=cover
        max_idx=i
print(coords[max_idx + 1] - 1)