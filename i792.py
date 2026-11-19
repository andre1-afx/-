N=int(input())
L=list(map(int,input().split()))
W=list(map(int,input().split()))
L.sort(reverse=True)
totalW=0
ans=0
for i in range(1,N):
    totalW+=W[i-1]
    ans+=L[i]*totalW
print(ans)
