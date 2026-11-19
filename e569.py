from collections import deque
import sys
import re

texts = sys.stdin.read()
lines = texts.split("\n")
voc = deque()

for x in lines:
    if x.strip() == "0":
        break

    res = []
    for tok in re.findall(r"[A-Za-z]+|[0-9]+|[^A-Za-z0-9]+", x):
        if tok.isalpha():          # 單字：輸出，放最前面
            voc.appendleft(tok)
            res.append(tok)
        elif tok.isdigit():        # 數字：取第 n 個，移到最前面
            n = int(tok)
            w = voc[n - 1]         # 編號從 1 開始
            del voc[n - 1]
            voc.appendleft(w)
            res.append(w)
        else:                      # 其他字元：原樣輸出
            res.append(tok)

    print("".join(res))
