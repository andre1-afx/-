

import sys
from bisect import bisect_left #二分搜尋法
def solve():
    data=sys.stdin.read().split()
    n=int(data[0])
    if n==1 :
        print(0)
        print(0)
        return 
    m=n*(n-1)//2#整數除法
    dists=sorted(map(int,data[1:1+m]))
    W=dists[-1]
    solutions=[]

    def try_place(remaining,points,y):
        needed=sorted(abs(y-p) for p in points)#放入y時,:每次嘗試放入一個候選新點 y 時,臨時算出來的「如果 y 是真的,它跟目前所有已放置點之間應該存在的距離清單」。
        rem=remaining[:]
        for val in needed:
            idx=bisect_left(rem,val)#插在最左邊且符合排序的位置
            if idx < len(rem) and rem[idx] == val:
                rem.pop(idx)
            else:
                return None
        return rem#成功的話回傳 空白list不是none
    def backtrack(remaining, points):
        if not remaining:
            solutions.append(tuple(sorted(points)))
            return
        d = remaining[-1]  # 目前剩下的最大距離
        for y in {d, W - d}:#中間點只會介於d或W-d之間
            if y in points:#如果y嘗試過就跳過
                continue
            rem2 = try_place(remaining, points, y)   # 用完整 remaining，不要先切掉
            if rem2 is not None:
                points.append(y)#確認y為確定點
                backtrack(rem2, points)#rem2是少了一個剩下的點
                points.pop()

    backtrack(dists[:-1], [0, W])  # 這一刀只是扣掉「0與W這一對」對應的那個W值，是對的，保留

    uniq = sorted(set(solutions))
    print(*uniq[0])
    print(*uniq[-1])

solve()
                            