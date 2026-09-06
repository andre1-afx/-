N,Q=map(int,input().split())
a=list(map(int,input().split()))
prefix=[0]*(N+1)
prefix[0]=0
prefix_sq=[0]*(N+1)
prefix_sq[0]=0
current_sum=0
current_sqtotal=0
for i in range(0,N):
    current_sum+=a[i]
    current_sqtotal+=a[i]*a[i]
    prefix[i+1]=current_sum
    prefix_sq[i+1]=current_sqtotal
for i in range(Q):
    l,r=map(int,input().split())
    if(r==l):
        print("0")
        continue
    nums=r-l+1
    total=prefix[r]-prefix[l-1]
    sq_total=prefix_sq[r]-prefix_sq[l-1]
    average=total/nums
    Var=(2*nums*sq_total-2*total*total+nums*nums)//(2*nums*nums)
    print(Var)