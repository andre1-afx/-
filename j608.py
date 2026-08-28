import bisect
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N, K = int(data[idx]), int(data[idx+1])
    idx += 2
    L = [int(data[idx+i]) for i in range(N)]
    idx += N
    R = [int(data[idx+i]) for i in range(N)]
    idx += N

    activities = sorted(zip(R, L))  # 依結束時間排序

    machines = []  # 維持排序好的「每台機器目前結束時間」清單
    count = 0

    for r, l in activities:
        if len(machines) < K:
            bisect.insort(machines, r)
            count += 1
        else:
            # 找出「結束時間最大、但仍 < l」的機器 -> best fit
            pos = bisect.bisect_left(machines, l)
            if pos > 0:
                machines.pop(pos - 1)
                bisect.insort(machines, r)
                count += 1
            # else: 沒有符合資格的機器,跳過

    print(count)

main()
