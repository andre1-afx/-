x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
leftx=max(x1,x3)
rightx=min(x2,x4)
topy=min(y2,y4)
bottomy=max(y1,y3)
if topy>bottomy and rightx>leftx:
    area=(rightx-leftx)*(topy-bottomy)
    print(area)
else:
    print("banana")