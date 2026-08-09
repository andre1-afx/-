def op1(string):
     answer=""
     result=[string[i:i+2] for i in range(0,len(string),2)]
     for s in result:
          
          answer+=s[::-1]
     return answer
def op2(string):
    answer=""
    result=[string[i:i+2] for i in range(0,len(string),2)]
    for s in result:
            
            answer+=''.join(sorted(s))
    return answer
def op3(string):
    answer=""
    mid=len(string)//2
    
    #s[:mid]=前半 s[mid:]=後半
    part1=string[:mid]
    part2=string[mid:]
    for k in range(mid):
         answer+=part1[k]
         answer+=part2[k]
    return answer
S=input()
k=int(input())
for _ in range(k):
     n=int(input())
     if(n==0):
          S=op1(S)
     elif(n==1):
          S=op2(S)
     else :
          S=op3(S)
print(S)