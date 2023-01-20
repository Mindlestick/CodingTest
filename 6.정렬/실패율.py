#실패율
def solution(N, stages):
    answer = []
    arr=[]
    
    for i in range(N):
        a=0
        b=0
        for j in stages:
            if i+1==j:
                a+=1
            if i+1<=j:
                b+=1
        if b==0:
            arr.append((i+1,0))
        else:
            arr.append((i+1,a/b))
    arr=sorted(arr,key=lambda x: -x[1])
    answer=[i[0] for i in arr]
        
    return answer