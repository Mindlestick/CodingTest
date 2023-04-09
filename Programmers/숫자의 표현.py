def solution(n):
    answer = 0
    sum=0
    j=1
    while(j<=n):
        for i in range(j,n+1):
            sum+=i
            
            if sum==n:
                answer+=1
                sum=0
                break
            elif sum>n:
                sum=0
                break
        j+=1
    
    return answer