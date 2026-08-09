def nextdir(maze,current,score,M,N,k,index):
    index=index%4
    x,y=current[0],current[1]
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    
        #右轉一次
    nx=x+directions[index][0]
    ny=y+directions[index][1]
    if( 0<=nx<M and 0<=ny<N ):
        if(maze[nx][ny]!=-1):
         return nx,ny,index
        else:
         return  nextdir(maze,(x,y),score,M,N,k,index+1)
         
    else:
        
        return nextdir(maze,(x,y),score,M,N,k,index+1)

line=input()
M,N,k,r,c=map(int,line.split())

jewels=0
collections=0
currentposition=(r,c)

#maze 裡面放寶石量
maze=[]
for _ in range(M):
     row=list(map(int,input().split()))
     maze.append(row)

x,y=r,c
score=0
index=0
while(maze[x][y]!=0):
    score+=maze[x][y]
    
    collections+=1
    maze[x][y]-=1
    if(score%k==0):
            index+=1
            index=index%4
    x,y,index=nextdir(maze,(x,y),score,M,N,k,index)
print(collections)