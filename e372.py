a = input().strip()
b = input().strip()
x, y, z = input().split()
s, t = input().split()
N = int(input())

def claim(num):
    if num == a:
        return 10_000_000
    if num == b:
        return 2_000_000
    if num in (x, y, z):
        return 200_000
    for k, prize in ((7, 40000), (6, 10000), (5, 4000), (4, 1000), (3, 200)):
        if num[-k:] in (x[-k:], y[-k:], z[-k:]):
            return prize
    if num[-3:] in (s, t):
        return 200
    return 0

upper = lower = 0
for _ in range(N):
    num = input().strip()
    if "*" in num:
        prizes = [claim(num.replace("*", str(d))) for d in range(10)]
        upper += max(prizes)
        lower += min(prizes)
    else:
        p = claim(num)
        upper += p
        lower += p

print(upper, lower)
#56337787
#93339845 83390355 80431063
#984 240
#4
#46356460
#56337787
#93339845
#12345240