from bisect import bisect_left
P=1299709
is_prime=[True]*(P+1)
is_prime[0]=False
is_prime[1]=False
i=2
while i*i<=P:
    square=i*i
    for j in range(square,P+1,i):
        is_prime[j]=False
    i+=1
while True:
    k=int(input())
    if k==0:
        break
    if is_prime[k]:
        print("0")
        continue
    p=k-1
    while not is_prime[p]:
        p-=1
    q=k+1
    while not is_prime[q]:
        q+=1
    print(q-p)

