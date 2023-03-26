def solution(food):
    answer = ''
    for f in range(len(food)):
        r=food[f]//2
        if r>0:
            for i in range(r):
                answer+=str(f)
    ranswer=answer[::-1]
    answer=answer+'0'+ranswer
    return answer