#같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if answer[-1]==i:
            continue
        else:
            answer.append(i)

    return answer