from collections import deque
def solution(priorities, location):
    answer = 0
    p=deque(priorities)
    idx=deque([i for i in range(len(priorities))])
    q=[]
    
    if priorities.index(max(p))==location:
        return 1
    
    while(len(p)):
        m=max(p)
        tmp=p.popleft()
        tmpi=idx.popleft()
        
        if tmp >= m:
            q.append(tmpi)
        
        else:
            p.append(tmp)
            idx.append(tmpi)
    
    answer=q.index(location)+1
    return answer