def is_bst(v, lo, hi):
    if v is None:
        return True
    if not (lo < v < hi):
        return False
    return is_bst(left.get(v), lo, v) and is_bst(right.get(v), v, hi)

def f(v):
    if v is None:
        return {('B', 0): 1}
    L = f(left.get(v))
    R = f(right.get(v))
    res = {}
    for (cl, hl), cntL in L.items():
        for (cr, hr), cntR in R.items():
            if hl != hr:
                continue
            ways = cntL * cntR
            key = ('B', hl + 1)
            res[key] = res.get(key, 0) + ways
            if cl == 'B' and cr == 'B':
                key = ('R', hl)
                res[key] = res.get(key, 0) + ways
    return res

case = 0
while True:
    try:
        n = int(input())
    except (EOFError, ValueError):
        break
    case += 1

    left = {}
    right = {}
    children = set()
    all_nodes = set()
    isrbtree = True

    if n == 1:
        print(f"Case {case}:1")
        continue

    for i in range(n - 1):
        P, S = map(int, input().split())
        children.add(S)
        all_nodes.add(S)
        all_nodes.add(P)
        if not isrbtree:
            continue
        if S < P:
            if P in left:
                isrbtree = False
            else:
                left[P] = S
        else:
            if P in right:
                isrbtree = False
            else:
                right[P] = S

    root = (all_nodes - children).pop()

    if not isrbtree or not is_bst(root, -1000, 1000):
        print(f"Case {case}:0")
        continue

    table = f(root)
    answer = 0
    for (c, h), cnt in table.items():
        if c == 'B':
            answer += cnt
    print(f"Case {case}:{answer}")