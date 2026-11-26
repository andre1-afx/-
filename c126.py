preorder=[]
inorder=[]
def post(pre,ino):
    
    if pre=="" and ino=="":
        return ""
    elif len(pre)==1 and pre==ino:
        return pre
    
    ch=pre[0]
    root=ino.index(ch) #pre=BAC INO=ABC 
    ino_left=ino[:root]
    
    pre_left=pre[1:1+len(ino_left)]
    mid=1+len(ino_left)
    ino_right=ino[root+1:]
    pre_right=pre[mid:]
    
    
    return post(pre_left,ino_left)+post(pre_right,ino_right)+pre[0]
while True:

    try:
        preorder, inorder = input().split()
    except EOFError:
        break
    print(post(preorder, inorder))

