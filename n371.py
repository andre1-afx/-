import sys
def main():
    data = sys.stdin.buffer.read().split()
    N, M = int(data[0]), int(data[1])
    nxt = [0] + list(range(2, N + 2)) + [N + 1]   # nxt[i] = i 右邊的人，N+1 表示沒有
    fallen = bytearray(N + 2)
    out = []
    for k in range(2, M + 2):
        x = int(data[k])
        if fallen[x]:
            out.append("我大意了啊~沒有閃"); continue
        a = nxt[x]
        if a > N or nxt[a] > N:
            out.append("來~ 騙"); continue
        t = nxt[a]
        fallen[t] = 1
        nxt[a] = nxt[t]          # 拆掉 t
        out.append(str(t))
    sys.stdout.write("\n".join(out) + "\n")
main()
    