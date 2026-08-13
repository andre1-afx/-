
from collections import deque
import sys
n=int(input())


line=sys.stdin.readline()
nums=list(map(int,line.split()))
unique=list(set(nums))
unique.sort()
d=deque(unique)
max=d[-1]
mind=([0,max])
maxd=([0,max])


def gendeque(mind,maxd,d,distance):
    
    distance+=d[0]
    mind.append(0+distance)
    maxd.append(max-distance)
    d.popleft()
    if(len(maxd)==n and len(mind)==n):
        return mind,maxd
    else :
        return gendeque(mind,maxd,d,distance)

dq1,dq2=gendeque(mind,maxd,d,0)
ans1=list(dq1)
ans1.sort()
ans2=list(dq2)
ans2.sort()
print(*ans1)
print(*ans2)