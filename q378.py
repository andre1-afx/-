N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    
    for j in range(1,N+1):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+min(a[i-1],b[j-1]))
print(dp[N][N])