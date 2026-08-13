n, t = map(int, input().split())
line = input()
nums = list(map(int, line.split()))

st = []
ans = 0
for x in nums:
    while st and st[-1] <= x:#只要stack不是空的且倒數第一個元素<=x,我們的答案加上最後一個元素
        ans += st[-1]
        x += st[-1]
        st.pop()
    if x <= t:
        st.append(x)
print(ans + sum(st))#ans是搬運過程,sum(st)是最後沒得交換的幾個沙包