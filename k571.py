N,K=map(int,input().split())
data=list(map(int,input().split()))
non_two_count,left,right,max_length=0,0,0,0
for right in range(N):
    if data[right]!=2:
        non_two_count+=1
    while non_two_count>K:
        if data[left]!=2:
            non_two_count-=1
        left+=1
    current_length=right-left+1
    max_length=max(max_length,current_length)
print(max_length)