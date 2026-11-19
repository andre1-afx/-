m=int(input())
for _ in range(m):
    N=int(input())
    dot=[]
    co=[]
    weights=[0]*N
    
    totalw=0
    total=0
    for i in range(N):
        a,x=map(int,input().split())
        
        totalw+=a

        
        d=x//a
        
        dot.append((a,d))
    dot.sort(key=lambda x:x[1])
    current=0
    x=0
    for i in range(N):
        current+=dot[i][0]
        if ((current*2)>=(totalw)):
            x=dot[i][1]
            break
    for j in range(N):
        total+=dot[j][0]*abs(dot[j][1]-x)
    print(total)