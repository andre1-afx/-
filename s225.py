import sys
from array import array
 
def main():
    stdin = sys.stdin.buffer
 
    first_line = stdin.readline().split()
    n = int(first_line[0])
    k = int(first_line[1])
 
    p_line = stdin.readline().split()
    p = [0] + [int(x) for x in p_line]   # p[1..k]
 
    # 用 array('i', ...) 存 cost 矩陣,存的是「原始C int」,不是Python物件
    # 一個 int 只佔 4 bytes,而不是像 list 那樣每個元素都要有物件開銷
    # 攤平成一維:cost 節點 u 到 v (1-indexed) 的值放在 cost[(u-1)*n + (v-1)]
    cost = array('i', bytes(4 * n * n))  # 先配置好固定大小的空間
 
    for i in range(n):
        # 一行一行讀,讀完這行、轉完數字之後,這行的暫存列表就沒人參照了
        # 會被直接回收,不會累積在記憶體裡
        row = stdin.readline().split()
        base = i * n
        # 用 map(int, row) 批次轉換,再一次整段塞進 array(切片賦值)
        # 比逐一 cost[base+j] = int(row[j]) 快很多,因為批次操作是用C實作的迴圈
        cost[base: base + n] = array('i', map(int, row))
 
    def get_cost(u, v):
        # u, v 是 1-indexed 節點編號
        return cost[(u - 1) * n + (v - 1)]
 
    INF = float('inf')
 
    # dp[idle] = 走到目前任務為止,「閒置者停在 idle」時的最小總花費
    dp = {1: 0}
    prev = 1
 
    for i in range(1, k + 1):
        cur = p[i]
        new_dp = {}
        # 把 cost 查表直接內聯(inline),避免每次呼叫 get_cost() 產生的函式呼叫開銷
        cost_prev_cur = cost[(prev - 1) * n + (cur - 1)]
        cur_minus1_n = (cur - 1)  # cur-1,重複用到
 
        for idle_old, val in dp.items():
            # 情況1:前線的人繼續跑
            cand1 = val + cost_prev_cur
            old1 = new_dp.get(idle_old, INF)
            if cand1 < old1:
                new_dp[idle_old] = cand1
 
            # 情況2:閒置的人換去跑
            cand2 = val + cost[(idle_old - 1) * n + cur_minus1_n]
            old2 = new_dp.get(prev, INF)
            if cand2 < old2:
                new_dp[prev] = cand2
 
        dp = new_dp
        prev = cur
 
    ans = INF
    for idle, val in dp.items():
        total = val + get_cost(prev, n) + get_cost(idle, n)
        if total < ans:
            ans = total
 
    print(ans)
 
if __name__ == "__main__":
    main()
