from collections import deque
def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)

    diff = sum(que1) - sum(que2)
    answer = 0
    leng=len(que1)

    while diff != 0:
        if diff > 0:  # 1이 더 큼
            num = que1.popleft()
            que2.append(num)
            diff = diff - num * 2
            answer += 1
        else:  # 2가 더큼
            num = que2.popleft()
            que1.append(num)
            diff = diff + num * 2
            answer += 1

        if answer > leng * 3:
            return -1

    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2))
