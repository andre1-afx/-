import sys
def evaluate_sum(s):
    total=0
    parts=split_top_level(s,"+")
    for v in parts:
        total+=evaluate_term(v)
    return total
def evaluate_no_f(expr):
    groups=expr.split("*")
    result=1
    for s in groups:
        partsum=evaluate_sum(s)
        result*=partsum
    return result
def split_top_level(s, delimiter):
    """依 delimiter 切開字串，但忽略括號內的 delimiter"""
    parts = []
    stack = []
    current = ""
    for char in s:
        if char == "(":
            current+=char
            stack.append(char)
        elif char == ")":
            current+=char
            stack.pop()
        elif char == delimiter and not stack:
            
            parts.append(current)
            current=""
        else:
            current+=char
    parts.append(current)
    return parts
def evaluate_term(term):
    if term.startswith("f("):
        inner=term[2:-1]
        args_str=split_top_level(inner,",")
        args_val=[evaluate(u) for u in args_str] 
        result=max(args_val)-min(args_val)
        return result
    else :
        return int(term)
def evaluate(expr):
     groups=split_top_level(expr,"*")
     result=1
     for a in groups:
         partsum=evaluate_sum(a)
         result*=partsum
     return result
line=sys.stdin.read().strip()
print(evaluate(line))


