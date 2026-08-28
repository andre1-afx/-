import sys
input = sys.stdin.readline

while True:
    line=input().strip()
    if(line=="-1"):
        break
    N,E=map(int,line.split())
    food=N*E
    dp=[0]*(food+1)
    for i in range(E+1):
        dp[i]=i#dp[0]=0,dp[1]=1....dp[E]=E
    
    
    for i in range(E+1,N*E+1):
        
        j=-(-i//E)
        
        dp[i]=dp[i-j]+1
    print(dp[food])
            


        



 