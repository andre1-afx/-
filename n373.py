import sys
MAXD=20
def link(a,b):
    if a[0]>b[0]:
        b,a=a,b
    a[1].append(b)
    return a
def add(heap,tree,d):
    while heap[d]:
        tree=link(tree,heap[d])
        heap[d]=None
        d+=1
    heap[d]=tree
def find_kth(heap,k):
    cnt=0
    for d in range(MAXD):
        if heap[d]:
            cnt+=1
            if cnt==k:
                return d 
def remove_kth(heap, k):
    d = find_kth(heap, k)
    t = heap[d]
    heap[d]=None
    for j in range(d):
        add(heap,t[1][j],j)
    # 1. 把 heap[d] 清成 None
    # 2. 對 j 從 0 跑到 d-1：
    #      用 add 把 t[1][j] 放回 heap，起點是隔間 j
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heap = [None] * MAXD
    out = []
    for i in range(1, n + 1):
        x = int(data[i])
        if x >= 0:
            add(heap,[x,[]],0)
              # 一行：把 1 張的新書放進隔間 0
        else:
            remove_kth(heap,-x)
              # 一行：拿第 -x 本
        roots = [t[0] for t in heap if t]
        out.append(' '.join(map(str, [len(roots)] + roots)))
    print('\n'.join(out))
main()