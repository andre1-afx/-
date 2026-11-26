import sys

data = sys.stdin.read().split()
idx = 0
out = []

while True:
    n = int(data[idx]); idx += 1
    if n == 0:                    # 結尾只有一個 0，拿到就停
        break
    q = int(data[idx]); idx += 1

    a = [int(x) for x in data[idx:idx + n]]   # 一次拿 n 個數字
    idx += n

    # 這裡做預處理
    i=0
    j=0
    start=[]
    end=[]
    cnt=[]
    bid=[0]*n
    
    while i<len(a):
        while j<len(a) and a[j]==a[i]:
            
            bid[j]=len(start)
            j+=1
        start.append(i)
        end.append(j-1)
        cnt.append(j-i)
        
        i=j
    m = len(cnt)
    sp = [cnt]                 # 第 0 層
    k = 1
    while (1 << k) <= m:       # 1 << k 就是 2 的 k 次方，區間長度不能超過 m
        prev = sp[-1]          # 上一層
        half = 1 << (k - 1)    # 一半的長度
        # 這一層有 m - (1 << k) + 1 格
        layer=[]
        for x in range(m - (1 << k) + 1):
            layer.append(max(prev[x], prev[x + half]))
        # 第 x 格 = max(prev[x], prev[x + half])
        sp.append(layer)
        k += 1
    for _ in range(q):
        i = int(data[idx]); j = int(data[idx + 1])
        idx += 2
        i -= 1; j -= 1            # 題目位置從 1 開始，串列從 0 開始
        # 這裡算答案
        # out.append(str(答案))
        bi,bj=bid[i],bid[j]
        if (bi==bj):
            
            out.append(str(j - i + 1))
            continue
            
        left=end[bi]-i+1
        right=j-start[bj]+1
        ans=max(left,right)
        L=bi+1
        R=bj-1
        if L<=R:
            t = (R - L + 1).bit_length() - 1
            ans=max(ans,sp[t][L],sp[t][R - (1 << t) + 1])
        out.append(str(ans))
sys.stdout.write("\n".join(out) + "\n")