N=map(int,input().split())
weights=list(map(int,input().split()))


#sum(current,total,target) total==sum return 1 else if total<sum sum(current下一個,total+current,target) current>sum return 0
if sum(weights)%2==1:
    print("0")
else:
    sideweight=sum(weights)//2
    dp=[False]*(sideweight+1)
    dp[0]=True
    for w in weights:
        for j in range(sideweight,w-1,-1):
            dp[j] = dp[j] or dp[j-w]
    print(1 if dp[sideweight] else 0)
    
    