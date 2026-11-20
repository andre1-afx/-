T=int(input())

while T>0:
    n=int(input())
    upper_bound=n
    lower_bound=0
    ans=-1
    
    while lower_bound<=upper_bound:
        mid=(upper_bound+lower_bound)//2
        target=(mid**2+mid)//2
        if(target<n):
            lower_bound=mid+1
        elif(target>n):
            upper_bound=mid-1
        if(target==n):
            ans=mid
            break
    if(ans==-1):
        ans=upper_bound
    print(ans)

    T-=1