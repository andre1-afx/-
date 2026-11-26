while(True):
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    a, b = min(n, m), max(n, m)
    samerow=n*m*(m-1)
    samecol=m*n*(n-1)
    sameline=2*a*(a-1)*(a-2)//3+(b-a+1)*a*(a-1)
    answer=(samerow+samecol+2*sameline)
    print(answer)