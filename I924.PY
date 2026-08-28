N,M=map(int,input().split())
restrict=N+M-2
answer=0


dp=[0]*M
    
row=list(map(int,input().split()))
dp[0]=row[0]
    
for j in range(1,M):
        dp[j]=dp[j-1]+row[j]#走到這裡的最佳解只有從左邊來的可能
for i in range(1, N):
        row = list(map(int, input().split()))
        dp[0]+=row[0]#加每一列的第一個
        for j in range(1,M):
            dp[j]=max(dp[j-1],dp[j])+row[j]#dp[j-1]是左邊來的,dp[j]是上一行的同個位置來的
print(dp[M-1])




    