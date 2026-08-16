from collections import deque
MAXN=52005
adj=[[] for _ in range(MAXN)]#每個節點接到哪些節點,至於節點的種類在其他地方另存
in_degree=[0]*MAXN#每個節點的入度(輸入數量)
received=[0]*MAXN
signal=[0]*MAXN
path_length=[0]*MAXN

gate_type=[0]*MAXN #哪一個節點對應哪一種閘門
is_terminal=[False]*MAXN
isGate=[False]*MAXN
p,q,r,m=map(int,input().split())
storedingate=[[] for _ in range(MAXN)]
for i in range(p+1,p+q+1):
    isGate[i]=True
for i in range(p+q+1,p+q+r+1):
    is_terminal[i]=True
values=list(map(int,input().split()))
for i in range(1,p+1):
    signal[i]=values[i-1]
gate=list(map(int,input().split()))
for i in range(p+1,p+q+1):

    values_index = i - (p + 1)    # 算出這個 i 對應到 values 這個 list 的第幾個位置(從0開始)
    gate_type[i] = gate[values_index]
for _ in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    in_degree[b]+=1
d=deque()
for i in range(1,p+1):
    d.append(i)
    path_length[i]=0
max_path_length=0
while d:
    u=d.popleft()
    
        
    for v in adj[u]:
        #v 是指向的閘門或終點
        add_len = 1 if isGate[v] else 0
        path_length[v] = max(path_length[v], path_length[u] + add_len)
        if is_terminal[v]:
            max_path_length=max(max_path_length,path_length[v]) 
            signal[v]=signal[u]
        received[v]+=1
        
        storedingate[v].append(signal[u])
        if gate_type[v]==1:
            if len(storedingate[v])==2 and sum(storedingate[v])==2:
                signal[v]=1
            else :
                signal[v]=0
        elif gate_type[v]==2:
            if len(storedingate[v])==2 and sum(storedingate[v])>=1:
                signal[v]=1
            else :
                signal[v]=0
        elif gate_type[v]==3:
            if len(storedingate[v])==2 and sum(storedingate[v])==1:
                        signal[v]=1
            else :
                        signal[v]=0
        elif gate_type[v]==4:
                    if len(storedingate[v])==1 and storedingate[v][0]==1:
                        signal[v]=0
                    else :
                        signal[v]=1
        if received[v]==in_degree[v] :
             d.append(v)
print(max_path_length)
for i in range(p+q+1,p+q+r+1):
     print(signal[i],end=' ')