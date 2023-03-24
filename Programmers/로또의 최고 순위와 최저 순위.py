def solution(lottos, win_nums):
    d={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt=0
    zero=0
    for i in lottos:
        if i==0:
            zero+=1
        elif i in win_nums:
            cnt+=1
            
    a,b=0,0
    a=d[cnt+zero]
    b=d[cnt]
    answer=[a,b]

    return answer