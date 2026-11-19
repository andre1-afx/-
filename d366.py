
LIMIT=31623
is_prime=[True]*(LIMIT+1)
is_prime[0]=is_prime[1]=False
p=2
while p*p<=LIMIT:
        if(is_prime[p]):
            for m in range(p*p,LIMIT+1,p):
                is_prime[m]=False
        p+=1
primes = [i for i in range(LIMIT + 1) if is_prime[i]]   

def count_divisors(x):
     n=x
     ans=1
     for p in primes:
          if p*p>n :
               break
          e=0
          while n%p==0:
               n//=p
               e+=1
          ans*=(e+1)
     if(n>1):
          ans*=2
     return ans

    
N=int(input())
while N>0:
    L,U=map(int,input().split())
    best=-1
    p=L
    for i in range (L,U+1):
        d=count_divisors(i)
        if(d>best):
             best=d
             p=i
    print(f"Between {L} and {U}, {p} has a maximum of {best} divisors.")
    N-=1