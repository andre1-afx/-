S = input()
N = int(input())
cakes = []
for i in range(N):
    cakes.append(input())

dp = [False] * (len(S) + 1)
dp[0] = True  # 空字串算切完

for i in range(1, len(S) + 1):
    for c in cakes:
        L = len(c)
        if i >= L and dp[i - L] and S[i - L:i] == c:
            dp[i] = True
            break

if dp[len(S)]:
    print("yes")
else:
    print("no")          
        

    



    
    

