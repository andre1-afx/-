t=int(input())
for _ in range(t):
    N,Q=map(int,input().split())

    cards=[]
    for i in range(Q):
            L,R,D=map(int,input().split())
            if D==1 :
                cards.append(L)#L開始翻轉
                cards.append(R+1)#r+1結束翻轉
    cards.sort()


    isodd=True
    oddnumbers=0
    evennumbers=0
    
    for i in range(len(cards)-1):
        if isodd:
            oddnumbers+=cards[i+1]-cards[i]
        isodd=not isodd
    evennumbers=N-oddnumbers 
    print(abs(evennumbers-oddnumbers))