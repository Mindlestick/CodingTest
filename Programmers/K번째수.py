def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        s=array[commands[i][0]-1:commands[i][1]]
        s.sort()
        answer.append(s[commands[i][2]-1])

    return answer