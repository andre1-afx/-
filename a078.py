import sys

alphabet=input().strip()
L=int(input().strip())
S=input().strip()
K=len(alphabet)
letter_index={ch:i for i,ch in enumerate(alphabet)}
trie=[{}]#list of dict
def insert(start):
    cur=0
    for i in range(L):
        c=letter_index[S[start+i]]
        if c not in trie[cur]:
            trie[cur][c]=len(trie)#這個是編號,c是字母,cur是目前是第幾個節點的意思
            trie.append({})#這個是增加新的空白字串
        cur=trie[cur][c]
n=len(S)
for start in range(n-L+1):
    insert(start)
result=[]
def dfs(node,depth):
    for idx in range(K):#前綴
        if idx not in trie[node]:
            result.append(alphabet[idx])
            result.extend(alphabet[0]*(L-depth-1))
            return True
        child=trie[node][idx]#後綴
        if depth+1==L:
         continue
        result.append(alphabet[idx])
        if dfs(child,depth+1):#這裡每一步遞迴要變更的是長度
            return True
        result.pop()#走錯了回頭的意思
    return False
dfs(0,0)
print(''.join(result))
