from collections import Counter


def turn(string,vector):
        vector=vector%len(string)
        return string[-vector:]+string[:-vector]


def scoreboard(*string):
       total=0      
       for chars in zip(*string):
              counter=Counter(chars)
              _,count=counter.most_common(1)[0]
              total+=count
       return total      
line=input()
m,n,k=map(int,line.split())
roulettes=[]

for _ in range(m):
        roulette=input()
        roulettes.append(roulette)
total_score=0
for i in range(k):
        nums=list(map(int,input().split()))
        for j in range(m):
            roulettes[j]=turn(roulettes[j],nums[j])
            
        total_score+=scoreboard(*roulettes)

print(total_score)
        