N,T,L,R=map(int,input().split())
w=list(map(int,input().split()))
hi=sum(w)
lo=max(w)
def can_split(max_sum):
    count=1
    current=0
    for x in w:
        if current+x>max_sum:
            count+=1#切段
            current=x#從新的x開始新一段
        else:
            current+=x
    return count<=T
while lo<hi:
    mid=(lo+hi)//2
    if can_split(mid):
        hi=mid
    else:
        lo=mid+1
if lo>=L and lo<=R:
    print(lo)
elif lo<L :
    print(L)
elif lo>R:
    print("-1")