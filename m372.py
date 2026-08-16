#建表使用union-find找集合
import sys
def solve():
    input_data=sys.stdin.read().split('\n')
    n,m=map(int,input_data[0].split())
    grid=[input_data[i+1] for i in range(n)]
    openings={
        'X': (True, True, True, True),
        'I': (True, True, False, False),
        'H': (False, False, True, True),
        'F': (False, True, False, True),   # 右和下
        '7': (False, True, True, False),   # 左和下
        'L': (True, False, False, True),   # 右和上
        'J': (True, False, True, False),   # 左和上
        '0': (False, False, False, False),

    }
    parent=list(range(n*m))
    size=[1]*(n*m)
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x#直到x=root回傳
    def union(x,y):
        rx,ry=find(x),find(y)
        if rx==ry :
            return
        if size[rx]<size[ry] :
            rx,ry=ry,rx#確保x是比較大的那個
        parent[ry]=rx
        size[rx]+=size[ry]#大吞小
    for i in range(n):
        for j in range(m):
            u_i,d_i,l_i,r_i=openings[grid[i][j]]#grid[i][j]表示是甚麼形狀,u,d,l,r分別代表缺口
            idx=i*m+j
            if j+1<m:
                u2,d2,l2,r2=openings[grid[i][j+1]]
                if r_i and l2:
                    union(idx,idx+1)
            if i+1<n:
                            u2,d2,l2,r2=openings[grid[i+1][j]]
                            if d_i and u2:
                                union(idx,idx+m)#差m個
            
    ans=max(size[find(i)]for i in range (n*m))
    print(ans)
solve()