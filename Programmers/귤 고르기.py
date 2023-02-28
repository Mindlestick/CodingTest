def solution(k, tangerine):
    s=set(tangerine)
    d=dict()
    
    for i in tangerine:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    d1=sorted(d.items(),key=lambda x:-x[1])
    d=dict(d1)
    
    
    answer = 0
    for i in d:
        answer+=1
        if k<0:
            break
            
        if d[i]>=k:
            break
        else:
            k-=d[i]
    
    return answer