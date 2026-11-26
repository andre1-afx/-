import sys
from collections import defaultdict
data = sys.stdin.read().split()
idx = 0
out = []
def find_d(S, n):
    pairs = defaultdict(list)
    for i in range(n):
        a = S[i]
        for j in range(i + 1, n):
            if S[j] == a:
                continue
            b = S[j]
            pairs[a + b].append((a, b))
    S.sort(reverse=True)
    for i in range(n):
        d = S[i]
        for j in range(n):
            if S[j] == d:
                continue
            c = S[j]
            key = d - c
            if key in pairs:
                for x, y in pairs[key]:
                    if x not in (d,c) and y not in (d,c):
                        return str(d)
    return "no solution"
while True:
    n = int(data[idx]); idx += 1
    if n == 0:                      # 讀到 0 結束
        break
    S = [int(x) for x in data[idx:idx + n]]   # 一次拿 n 個

    idx += n
    # 這裡找 d，存進 out
    out.append(find_d(S,n))
sys.stdout.write("\n".join(out) + "\n")