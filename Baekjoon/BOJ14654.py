# 스테판 쿼리
n=int(input())
t1=list(map(int,input().split()))
t2=list(map(int,input().split()))
win=0
answer=1
m=0

for i in range(n):
    if abs(t2[i]-t1[i])==1:
        if max(t1[i],t2[i])==t1[i]:
            if win==1:
                answer+=1
            elif win==2:
                answer=1
            win=1
        else:
            if win==2:
                answer+=1
            elif win==1:
                answer=1
            win=2
        
    elif t1[i]==t2[i]:
        if win==1:
            win=2
        elif win==2:
            win=1
        answer=1
    
    else:
        if min(t1[i],t2[i])==t1[i]:
            if win==1:
                answer+=1
            elif win==2:
                answer=1     
            win=1
        else:
            if win==2:
                answer+=1
            elif win==1:
                answer=1
            win=2
         
    m=max(m,answer)
print(m)