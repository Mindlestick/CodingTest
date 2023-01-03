def solution(s):
    answer = []

    n=[]
    for i in range(len(s)):
        if s[i] in n:
            answer.append(i-s[:i].rindex(s[i]))
        else:
            n.append(s[i])
            answer.append(-1)

    return answer