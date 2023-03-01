def solution(elements):
    s=set()
    size = len(elements)
    e=elements *2
    #print(e)
    for i in range(1,size+1):
        for j in range(size):
            s.add(sum(e[j:j+i]))
    #print(s)
    answer = len(s)
    return answer