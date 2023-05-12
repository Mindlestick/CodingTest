# 곰곰이와 학식
a = list(map(int,input().split()))
x = list(map(int,input().split()))

answer=0
while(1):
    for i in range(3):
        if a[i]>=x[i]:
            answer+=x[i]
            a[i]-=x[i]
            x[i]=0
        else:
            answer += a[i]
            x[i]-=a[i]
            a[i]=0

    if x[0]<3 and x[1]<3 and x[2]<3 or sum(a)==0:
        break
    for i in range(3):
        if x[i]>2 and a[i]==0:
            x[(i+1)%3]=x[i]//3
            x[i]=x[i]%3

print(answer)