N=int(input())
neg_inf = float('-inf')
lower_bound=neg_inf
pos_inf = float('inf')
upper_bound=pos_inf
havetemp=True
for _ in range(N):
    C,D=map(int,input().split())
    if (D==1):
        if(C<upper_bound):
            upper_bound=C
    else:
        if (C>lower_bound):
            lower_bound=C
if (upper_bound-lower_bound)>0:
    print(upper_bound-lower_bound)
else:
    print("I am a robot.")