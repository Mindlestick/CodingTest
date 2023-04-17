def solution(s):
    answer = True
    q=[]
    
    if len(s)%2!=0:
        return False
    
    for i in s:
        if i=='(':
            q.append('(')
        elif i==')':
            if len(q)==0:
                return False
            q.pop()
    return len(q)==0