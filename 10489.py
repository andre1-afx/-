T=int(input())
while T>0:
    N,B=map(int,input().split())
    rem=0
    for i in range(B):
        line=list(map(int,input().split()))
        m=1
        for j in range(1,line[0]+1):
            line[j]%=N
            m=(m*line[j])%N
        rem+=m%N
        rem%=N
    print(rem)
    T-=1
