# 디펜스 게임
from queue import PriorityQueue
def solution(n, k, enemy):
    size=0
    if k>=len(enemy):
        return len(enemy)

    q = PriorityQueue()
    for i in range(len(enemy)):
        q.put(enemy[i])
        size+=1
        if size>k:
            t=q.get()
            size-=1
            n-=t
        
        if n >= 0 :
            answer = i + 1
            
        if n <= 0 :
            break
    
    return answer