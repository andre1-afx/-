N,K=map(int,input().split())
cards=list(map(int,input().split()))
negcards=[card for card in cards if card<=0]
negcards.sort()
negsum=0
possum=0
poscards=[card for card in cards if card>0]
poscards.sort()
if K>=len(negcards) and negcards:
    
    K-=len(negcards)
    turnedcards=[-x for x in negcards]
    temp=turnedcards+poscards
    temp.sort()
    if K%2==1 and temp:
        possum=sum(temp)-2*temp[0]
    elif K%2==0 and poscards:
        possum=sum(temp)
elif K<len(negcards) and negcards:
    
    negsum=-1*sum(negcards[0:K])+sum(negcards[K:])
    if poscards:
        possum=sum(poscards)
elif not negcards and poscards:
    if K%2==0:
        possum=sum(poscards)
    else :
        possum=sum(poscards)-2*poscards[0]
elif not poscards and negcards:
    if K<len(negcards):
        negsum=-1*sum(negcards[0:K])+sum(negcards[K:])
    else:
        K-=len(negcards)
        negsum=-1*(sum(negcards))
        if K%2==1:
            negsum-=2*negcards[0]
        
print(possum+negsum)