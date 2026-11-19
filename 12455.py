N = int(input())
for _ in range(N):
    target = int(input())
    num = int(input())
    sticks = list(map(int, input().split()))           # 1. 轉成 list

    dp = [[False] * (target + 1) for _ in range(num + 1)]   # 2. 每一列各自獨立
    dp[0][0] = True

    for i in range(1, num + 1):
        for j in range(target + 1):
            if dp[i - 1][j]:                            # 3. 不拿第 i 根
                dp[i][j] = True
            if j - sticks[i - 1] >= 0 and dp[i - 1][j - sticks[i - 1]]:   # 拿第 i 根
                dp[i][j] = True

    if dp[num][target]:
        print("YES")                                    # 4. 不要多加 \n
    else:
        print("NO")
            

        
        
