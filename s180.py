import bisect
n,m=map(int,input().split())
t=list(map(int,input().split()))
t.sort()
shows=0
def binary_search(sch,day,isleftmost):
    left=0
    right=n
    while left<right:
        mid=(left+right)//2
        if isleftmost:
            cond=sch[mid]>=day
        else :
            cond=sch[mid]>day
        if cond :
            right=mid
        else :
            left=mid+1
    return left

for _ in range(m):
    #想法,在旅行團陣列找可以插入的地方(logn),m行,O(mlogn),個數:夾在中間的元素有幾個
    
    
    s,e=map(int,input().split())
    index1=binary_search(t,s,True)
    index2=binary_search(t,e,False)
    shows+=index2-index1
print(shows)


    
    
