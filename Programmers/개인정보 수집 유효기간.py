def Priv(date,today,n):
    dy,dm,dd=map(int,date.split('.'))
    ty,tm,td=map(int,today.split('.'))
    
    if dm+n>12:
        dy+=(dm+n)//12
        dm=(dm+n)%12
        if dm==0:
            dm=12
            dy-=1
    else:
        dm+=n
    #print(dy,dm,dd)
    #print(ty,tm,td)
    
    if dy < ty:
        return True
    elif dy==ty:
        if dm < tm:
            return True
        elif dm==tm:
            if dd <= td:
                return True 
    return False

def solution(today, terms, privacies):
    answer = []
    
    d=dict()
    for i in terms:
        c,n=i.split()
        d[c]=int(n)
        
    result=1
    for i in privacies:
        date,c = i.split()

        if Priv(date,today,d[c]):
            answer.append(result)
        result+=1

    return answer