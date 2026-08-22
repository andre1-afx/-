import sys


#關鍵是題目的前綴和有單調性,所以滿足第一個必滿足第二個
n,m=map(int,input().split())
input_data=list(map(int,input().split()))





prefixsum=0
prefix=[0]*(n+1)
for i in range (1,n+1):
   prefix[i]=prefix[i-1]+input_data[i-1]#input_data [i-1]就是自己
out=[]

#計算prefixsum,再利用二分搜對prefixsum找答案


for _ in range(m):
    l,r,a,b=map(int,sys.stdin.readline().split())
    
    base=prefix[l-1]
    total=prefix[r]-base#最後一項減之前的前綴和
    
    
    lo=l
    hi=r
    
    
    
    
    while lo<hi:
        mid=(lo+hi)//2

        if (prefix[mid] - base) * (a + b) >= a * total:
                hi = mid
        else:
                lo = mid + 1
    out.append(str(lo))
sys.stdout.write('\n'.join(out) + '\n')

    



