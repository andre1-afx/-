import sys
from functools import lru_cache

def solve():
    n, m, r, k, t = map(int, input().split())
    a = list(map(int, input().split()))
    N = m * r
    class_of = [i // r for i in range(N)]   # 學生 i (0-indexed) 屬於哪個班
    spec = [x - 1 for x in a]               # 專長改成 0-indexed，方便當 bit 位置

    def next_cnt(i, cur_cnt, took):
        # 這個 function 幫你算出「移動到 i+1 時，cnt 應該變成多少」
        # 提示：
        # 1. 如果 i+1 已經超出範圍(i+1 >= N)，回傳什麼都可以(不會再用到)
        # 2. 如果 i+1 跟 i 不同班，代表換了一個新班級，cnt 要歸零
        # 3. 如果 i+1 跟 i 同班，cnt 要看剛剛這個人 i 有沒有被選(took)，
        #    有選就 +1，沒選就維持 cur_cnt
        pass  # TODO

    @lru_cache(maxsize=None)
    def count(i, remain, mask, cnt):
        if remain == 0:
            return 1
        if i == N:
            return 0
        # TODO 1: 算「跳過第 i 人」貢獻的解數
        #   skip_cnt = next_cnt(i, cnt, took=False)
        #   total = count(i+1, remain, mask, skip_cnt)

        # TODO 2: 如果「選第 i 人」合法(專長沒用過 且 cnt < 2)，
        #   把「選他」貢獻的解數也加進 total
        #   take_cnt = next_cnt(i, cnt, took=True)
        #   total += count(i+1, remain-1, mask | (1 << spec[i]), take_cnt)

        return total  # TODO 3: 記得把上面兩塊組起來

    # ---- 用 count 定位第 t 筆解 ----
    result = []
    mask = 0
    cnt = 0
    remain = k
    rank = t   # 1-indexed

    for i in range(N):
        if remain == 0:
            break
        skip_cnt = next_cnt(i, cnt, took=False)
        ways_skip = count(i + 1, remain, mask, skip_cnt)

        if rank <= ways_skip:
            # 第 t 筆解落在「不選這個人」的分支裡
            cnt = skip_cnt
            continue
        else:
            rank -= ways_skip
            # 走到這裡代表「選這個人」一定是合法的
            result.append(i + 1)  # 輸出時要還原成 1-indexed 學生編號
            mask |= (1 << spec[i])
            remain -= 1
            cnt = next_cnt(i, cnt, took=True)

    print(*result)

solve()


