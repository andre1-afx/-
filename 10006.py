while True:
    n=int(input())
    isp=1
    fail=0
    i=2
    if (n==0):
        break
    while i*i<=n:
        if (n%i==0):
            
            isp=0
            break
        i+=1
    if isp:
         print(f"{n} is normal.")
         continue
    for a in range(2,n,1):
        if   pow(a,n,n)%n!=a:
                print(f"{n} is normal.")
                fail=1
                break
    if fail:
         continue
    print(f"The number {n} is a Carmichael number.")