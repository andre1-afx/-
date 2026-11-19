T=int(input())
round=1
while(T>=round):
    N,D=map(int,input().split())
    line=list(input().split())
    go=[0]
    back=[0]
    turn=0
    for stones in line:
        c,d=stones.split('-')
        d=int(d)
        if c=="B":
            go.append(d)
            back.append(d)
        elif c=="S":
            if turn==0:
                go.append(d)
            else:
                back.append(d)
        turn=1-turn
    go.append(D)
    back.append(D)
    max_gap=-1
    for i in range(len(go)-1):
        if (go[i+1]-go[i])>max_gap:
            max_gap=go[i+1]-go[i]
    for i in range(len(back)-1):
              if (back[i+1]-back[i])>max_gap:
                  max_gap=back[i+1]-back[i]
    print(f"Case {round}: {max_gap}")
    round+=1
