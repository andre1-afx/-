import sys, math

# 先把所有要問的 i 讀進來，讀到 -1 停
qs = []
for tok in sys.stdin.read().split():
    k = int(tok)
    if k == -1:
        break
    qs.append(k)

N = max(qs) if qs else 0          # 只需要算到最大的那個 i
x = [0] * (N + 1)
x[0] = 1

for i in range(1, N + 1):
    s = math.sin(i)
    x[i] = (x[int(i - math.sqrt(i))] + x[int(math.log(i))] + x[int(i * s * s)]) % 1000000

for k in qs:
    print(x[k])