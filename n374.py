import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    def nxt():
        nonlocal idx
        v = int(data[idx]); idx += 1
        return v

    N = nxt(); M = nxt()
    heights = [0]*(N+1)
    for i in range(1, N+1):
        heights[i] = nxt()

    order = sorted(range(1, N+1), key=lambda i: heights[i])

    pred = [[] for _ in range(N+1)]
    for _ in range(M):
        a = nxt(); b = nxt()
        if heights[a] < heights[b]:
            pred[b].append(a)
        else:
            pred[a].append(b)

    # 遞移歸約 (transitive reduction)：用 bitmask 存每個節點的祖先集合
    anc = [0]*(N+1)
    reduced_succ = [[] for _ in range(N+1)]

    for v in order:
        preds = pred[v]
        k = len(preds)
        if k == 0:
            continue
        if k == 1:
            u = preds[0]
            anc[v] = anc[u] | (1 << u)
            reduced_succ[u].append(v)
            continue
        prefix = [0]*(k+1)
        suffix = [0]*(k+2)
        for i in range(k):
            prefix[i+1] = prefix[i] | anc[preds[i]]
        for i in range(k-1, -1, -1):
            suffix[i+1] = suffix[i+2] | anc[preds[i]]
        full_anc = 0
        for i in range(k):
            u = preds[i]
            other_or = prefix[i] | suffix[i+2]
            if not (other_or >> u) & 1:
                reduced_succ[u].append(v)
            full_anc |= anc[u] | (1 << u)
        anc[v] = full_anc

    reduced_pred = [[] for _ in range(N+1)]
    for u in range(1, N+1):
        for v in reduced_succ[u]:
            reduced_pred[v].append(u)

    # 前驅集合分組：相同前驅集合的節點共用一次計算
    content_to_gid = {}
    gid_to_predlist = [[]]
    group_id = [0]*(N+1)
    for v in order:
        plist = reduced_pred[v]
        if not plist:
            group_id[v] = 0
            continue
        key = tuple(sorted(plist))
        gid = content_to_gid.get(key)
        if gid is None:
            gid = len(gid_to_predlist)
            content_to_gid[key] = gid
            gid_to_predlist.append(plist)
        group_id[v] = gid

    num_groups = len(gid_to_predlist) - 1
    NG1 = num_groups + 1

    Q = nxt()
    out = []
    is_target = bytearray(N+1)

    order_local = order
    group_id_local = group_id
    gid_predlist_local = gid_to_predlist

    for _ in range(Q):
        D = nxt()
        targets = [nxt() for _ in range(D)]
        for a in targets:
            is_target[a] = 1

        dp_t = [-1]*(N+1)
        dp_x = [-1]*(N+1)
        computed = bytearray(NG1)
        gbt = [0]*NG1
        gbx = [0]*NG1

        for v in order_local:
            g = is_target[v]
            bt = g; bx = 1
            gid = group_id_local[v]
            if gid:
                if computed[gid]:
                    best_pt = gbt[gid]; best_px = gbx[gid]
                else:
                    best_pt = -1; best_px = -1
                    for u in gid_predlist_local[gid]:
                        put = dp_t[u]; pux = dp_x[u]
                        if put > best_pt or (put == best_pt and pux > best_px):
                            best_pt = put; best_px = pux
                    gbt[gid] = best_pt; gbx[gid] = best_px
                    computed[gid] = 1
                ct = best_pt + g; cx = best_px + 1
                if ct > bt or (ct == bt and cx > bx):
                    bt = ct; bx = cx
            dp_t[v] = bt
            dp_x[v] = bx

        bestt, bestx = -1, -1
        for i in range(1, N+1):
            dti = dp_t[i]
            if dti > bestt or (dti==bestt and dp_x[i]>bestx):
                bestt, bestx = dti, dp_x[i]
        out.append(f"{bestt} {bestx}")

        for a in targets:
            is_target[a] = 0

    sys.stdout.write("\n".join(out)+"\n")

main()