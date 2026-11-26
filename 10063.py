s=[]

results=[]
def p(cur,k,s):
    if k==len(s):
        out.append(cur)
        return
    for i in range(k+1):
        new= cur[:i] + s[k] + cur[i:]
        p(new,k+1,s)
        
while(True):
    
    try:
        s=input()
    except EOFError:
        break
    s=s.strip()
    
    out=[]
    p(s[0],1,s)
    results.append("\n".join(out))
print("\n\n".join(results))   