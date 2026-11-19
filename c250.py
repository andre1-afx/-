import sys
from bisect import bisect_right
from itertools import repeat
from operator import sub

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0]); p = 1; out = []
    for _ in range(t):
        n, k = int(data[p]), int(data[p + 1]); p += 2
        s = sorted(map(int, data[p:p + n])); p += n

        lo, hi = 0, s[-1] - s[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            # 對每個 s[j]，數有幾個 s[i] <= s[j] - mid，也就是差 >= mid 的配對
            cnt = sum(map(bisect_right, repeat(s, n), map(sub, s, repeat(mid, n))))
            if cnt >= k:
                lo = mid
            else:
                hi = mid - 1
        out.append(lo)
    print("\n".join(map(str, out)))

main()