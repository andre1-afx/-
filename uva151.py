from collections import deque
N=int(input())

while(N>0):
    
    for m in range(1,2*N):
        light=[True]*(N+1)
        light[1]=False
        
        index=1
            
        new_start=1
        round=1
        while (light[13]):
                index=new_start
                havelight=0
                while(havelight<=m):
                    if light[index] :
                        havelight+=1
                        if   havelight==m:
                            light[index]=False
                            new_start=(index)
                            break

                    
                    index=index%N+1
                round+=1
                
        if (round==N):
                print(m)
                break
    N=int(input())

