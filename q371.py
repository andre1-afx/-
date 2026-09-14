import sys
input = sys.stdin.readline
K,Q=map(int,input().split())
T=pow(2,K)
def solve(isright,isleft,o,x,low,idx):
    if (o==1):
        if x==pow(2,K-1):
            return -1
        if isleft:
            return x+low
        elif isright :
            return x-low
    if (o==2):
        if low==1:
            return -1
        else:
            return x-low//2
            
    if  (o==3):
        if low==1:
            return -1
        else:
            return x+low//2
    t=pow(2,idx)
    if (o==4):
            if x==t :
                return -1
            else:
                return x-low*2
    if (o==5):
            if x==T-t:
                 return -1
            else:
                return x+low*2
    if (o==6):
            return x*(2*low-1)
for _ in range(Q):
    o,x=map(int,input().split())
    low=x&(-x)
    idx=low.bit_length()-1
    isleft=False
    isright=False
    if ((x >> (idx+1)) & 1 )==1:
        isright=True
    else:
        isleft=True
    ans=solve(isright,isleft,o,x,low,idx)
    print(ans)
