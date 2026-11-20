import math
def compute(k):
    if(k==0):
        return 1
    return compute(int(k-math.sqrt(k)))+compute(int(math.log(k)))+compute(int(k*math.sin(k)*math.sin(k)))
while True:
    k=int(input())
    if(k==-1):
        break
    print(compute(k)%1000000)