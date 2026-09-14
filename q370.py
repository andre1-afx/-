x_string=input()

modnumber=[False]*10
current_mod=0
modnumber[0]=True
have5=False
for c in x_string:
    digit=int(c)
    current_mod=(current_mod+digit)%10
    if not modnumber[current_mod]:
        modnumber[current_mod]=True
    pair=(current_mod+5)%10
    if  modnumber[current_mod] and modnumber[pair]:
        have5=True
        print("耗子尾汁，好好反思")
        break

if not have5:
    print("謝謝朋友們")

