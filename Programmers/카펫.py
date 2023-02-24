def solution(brown, yellow):
    li = []    
    answer = []
    sum=brown+yellow

    for i in range(1, sum+1):
        if sum%i==0:
            li.append([i,sum//i])
    for i,j in li:
        if i>=j and (i-2)*(j-2)==yellow:
            return [i,j]
    return answer