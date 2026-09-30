N,K=map(int,input().split())
gifts=list(map(int,input().split()))
C=[0]*101

total=0
for i,x in enumerate(gifts):
    C[x]+=1
for x in C:
    total+=x//K
print(total)
