import sys
out=[]
def DFS(k,start,path):
    f=start
    while f*f<=k:
        if k%f==0:
            results.append(path+[f,k//f])
            DFS(k//f,f,path+[f])
        f+=1

for tok in sys.stdin.read().split():
    k=int(tok)
    if k==0:
        break
    results = []                          # 這個 N 的所有分解，每個是一個串列，例如 [2, 10]
    # ……DFS 把分解放進 results……
    DFS(k,2,[])
    results.sort()                        # 字典順序

    out.append(str(len(results)))         # 第一行：有幾種
    for f in results:
        out.append(" ".join(map(str, f))) # [2, 2, 5] 變成 "2 2 5"

sys.stdout.write("\n".join(out) + "\n")   # 最後一次印出