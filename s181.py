
import sys
from functools import lru_cache

def solve():
    n, m, r, k, t = map(int, input().split())
    a = list(map(int, input().split()))
    N = m * r
    class_of = [i // r for i in range(N)]
    spec = [x - 1 for x in a]  # 專長改成 0-indexed，方便當 bit 位置

    def next_cnt(i, cur_cnt, took):
        if i + 1 >= N:
            return 0  # 沒有下一位了，這個值不會再被用到
        if class_of[i] != class_of[i + 1]:
            return 0  # 換班了，歸零
        return cur_cnt + 1 if took else cur_cnt

    @lru_cache(maxsize=None)
    def count(i, remain, mask, cnt):
        if remain == 0:
            return 1
        if i == N:
            return 0
        total = 0
        # 不選第 i 人
        skip_cnt = next_cnt(i, cnt, took=False)
        total += count(i + 1, remain, mask, skip_cnt)
        # 選第 i 人（要合法：專長沒用過 且 這班還沒選滿 2 人）
        if not (mask >> spec[i]) & 1 and cnt < 2:
            take_cnt = next_cnt(i, cnt, took=True)
            total += count(i + 1, remain - 1, mask | (1 << spec[i]), take_cnt)
        return total

    # ---- 用 count 定位第 t 筆解 ----
    result = []
    mask = 0
    cnt = 0
    remain = k
    rank = t  # 1-indexed

    for i in range(N):
        if remain == 0:
            break
        # 先算「選第 i 人」這個分支能貢獻幾種解
        take_ways = 0
        if not (mask >> spec[i]) & 1 and cnt < 2:
            take_next = next_cnt(i, cnt, took=True)
            take_ways = count(i + 1, remain - 1, mask | (1 << spec[i]), take_next)

        if rank <= take_ways:
            # 第 rank 筆解落在「選第 i 人」這個分支
            result.append(i + 1)
            mask |= (1 << spec[i])
            remain -= 1
            cnt = next_cnt(i, cnt, took=True)
        else:
            # 落在「不選第 i 人」的分支，rank 要扣掉前面佔掉的
            rank -= take_ways
            cnt = next_cnt(i, cnt, took=False)

    print(*result)

solve()


