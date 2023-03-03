def solution(A,B):
    answer = 0
    s1=0
    s2=0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        s1+=A[i]*B[i]
        
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        s2+=A[i]*B[i]
    answer=min(s1,s2)
    
    return answer