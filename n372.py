N=int(input())
x=[0]*(N+1)
y=[0]*(N+1)
midterm=list(map(int,input().split()))
final=list(map(int,input().split()))
for i in range(N):
    x[midterm[i]]=i+1
    y[final[i]]=i+1
pts=[(x[s],y[s]) for s in midterm]
def solve(lo, hi):
    if hi - lo <= 3:
        d, cnt = float('inf'), 0
        for i in range(lo, hi):
            for j in range(i+1, hi):
                t=abs(pts[j][0]-pts[i][0])+abs(pts[j][1]-pts[i][1])
                  # 算 pts[i]、pts[j] 的曼哈頓距離 t，依上面三種情況更新 d、cnt
                if t<d:
                    d=t
                    cnt=1
                elif t==d:
                    cnt+=1
                

        return d, cnt
    mid = (lo + hi) // 2
    midx = pts[mid][0]
    dl, cl = solve(lo, mid)
    dr, cr = solve(mid, hi)
    if dl < dr:
        d, cnt = dl, cl
    elif dl > dr:
       
        d,cnt=dr,cr
    else:
        d,cnt=dr,cl+cr
    strip = []
    for q in pts[lo:hi]:
            if abs(q[0]-midx)<=d:   # q 的 x 離 midx 不超過 d
                strip.append(q)
    strip.sort(key=lambda q: q[1])
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] > d:
                break
            if (strip[i][0] < midx) == (strip[j][0] < midx):      # 兩點在同一半邊
                continue
            t = abs(strip[j][0]-strip[i][0])+abs(strip[j][1]-strip[i][1])     # 曼哈頓距離
            if t < d:
                d=t
                cnt=1
            elif t == d:
                cnt+=1
    return d, cnt
print(*solve(0, N))