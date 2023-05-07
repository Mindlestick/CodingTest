# 기념품
n=int(input())
q=[i for i in range(1,n+1)]

p=1
i=0
while(len(q)!=1):
    i+=(p**3)-1
    i%=len(q)
    q.remove(q[i])
    p+=1
print(q[0])