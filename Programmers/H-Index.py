def Up(x,s):
    cnt=0
    for i in s:
        if i>=x:
            cnt+=1
    return cnt

def Down(x,s):
    cnt=0
    for i in s:
        if i<=x:
            cnt+=1
    return cnt

def solution(citations):
    answer = 0
    for i in range(max(citations)):
        if Up(i,citations) >= i and Down(i,citations)<=i:
            answer=max(answer,i)
    return answer
