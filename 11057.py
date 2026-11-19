from collections import Counter
 
while True:
    try:
        s = input()
        while s.strip() == "":     # 是空行就再讀下一行
            s = input()
        n = int(s)
        
        line=list(map(int,input().split()))
        from collections import Counter
        cnt = Counter(line) 
        hash=set(line)
        find=0
        target=int(input())
        gap_min=1000000000
        low=0
        high=0
        for num in line:
            remain=target-num
            if remain in cnt:
                if remain == num and cnt[num] < 2:
                    continue  
                diff=max(remain,num)-min(remain,num)
                if diff<gap_min:
                    gap_min=diff
                    low=min(remain,num)
                    high=max(remain,num)
                    find=1
        
        print(f"Peter should buy books whose prices are {low} and {high}.")        
        print()
    except EOFError:
        break

