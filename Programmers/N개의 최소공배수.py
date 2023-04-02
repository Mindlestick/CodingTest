def solution(arr):
    answer = max(arr)
    cnt=0
    while(cnt!=len(arr)):
        for i in arr:
            if answer%i==0:
                cnt+=1
            else:
                answer+=1
                cnt=0
                break
    return answer