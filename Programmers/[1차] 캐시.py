from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        return len(cities)*5
    cache=deque()
    
    for i in cities:
        if i.lower() in cache:
            cache.remove(i.lower())
            cache.append(i.lower())
            answer+=1
        else:
            if len(cache)==cacheSize:
                cache.popleft()
            cache.append(i.lower())
            answer+=5
    
    return answer