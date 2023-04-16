from collections import deque
def isSymmetry(s):
    li=[]
    for i in s:
        if i =='[' or i== '{' or i=='(':
            li.append(i)
        else:
            if len(li)==0:
                return 0
        
        if i==']':
            if li[-1]=='[':
                li.pop()
            else:
                return 0
        if i=='}':
            if li[-1]=='{':
                li.pop()
            else:
                return 0
        if i==')':
            if li[-1]=='(':
                li.pop()
            else:
                return 0
        
    if len(li)==0:
        return 1
    return 0
            
def solution(s):
    answer = 0
    l=deque(s)
    r=deque()

    if len(s)%2==1:
        return 0
    
    for i in range(len(s)):
        answer+= isSymmetry(list(l+r))
        r.append(l.popleft())

    return answer