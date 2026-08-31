from bisect import bisect_left
N=int(input())
pyramid=[]
for i in range(N):
    t=tuple(map(int,input().split()))
    pyramid.append(t)
pyramid.sort(key=lambda t: (t[0], -t[1]))#key的意思是標準,lambda是匿名函式,函式的參數是t[0],-t[1],t[0]遞增,t[1]遞減
tails=[]
for t in pyramid:
    pos=bisect_left(tails,t[1])
    if pos==len(tails):
        tails.append(t[1])#是最大值放結尾
    else :
        tails[pos]=t[1]#不是最大值放更好的位置
print(len(tails))
