from bisect import bisect_right
n = int(input())
w = list(map(int, input().split()))
non_neg=[x for x in w if x>=0]
neg=[x for x in w if x<0]
S=max(-(sum(w)),0)
order=non_neg+neg
print(S)
print(*order)