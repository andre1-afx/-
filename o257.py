from bisect import bisect_left

N=int(input())
customers=[]
for i in range(N):
    
    a,b,c=map(int,input().split())
    customers.append((a,b,c))
customers.sort(key=lambda x:x[1])#依照x排序
ends=[x[1] for x in customers]
dp=[0]*(N+1)
for i in range(1,N+1):
    

        j=bisect_left(ends,customers[i-1][0])
    
        
        dp[i]=max(dp[i-1],dp[j]+customers[i-1][2])
print(dp[N])