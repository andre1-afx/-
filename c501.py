import sys

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    T = int(data[p]); p += 1
    out = []
    for _ in range(T):
        N, M = int(data[p]), int(data[p + 1]); p += 2
        balls = []
        for _ in range(N):
            d, c = int(data[p]), int(data[p + 1]); p += 2
            balls.append((d, c))
        balls.sort()

        cnt = [0, 0, 0, 0]          # cnt[1]~cnt[3] 是視窗裡各顏色的數量
        best = -1
        left = 0
        for right in range(N):
            cnt[balls[right][1]] += 1
            while cnt[1] >= M and cnt[2] >= M and cnt[3] >= M:
                length = balls[right][0] - balls[left][0]
                if best == -1 or length < best:
                    best = length
                cnt[balls[left][1]] -= 1
                left += 1
        out.append("QQ" if best == -1 else str(best))
    print("\n".join(out))

main()