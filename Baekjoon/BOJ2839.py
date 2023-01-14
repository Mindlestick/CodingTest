#2839 설탕 배달

n=int(input())

cnt=0

while(1):
    if n%5==0:
        cnt=cnt+n//5
        break
    n=n-3
    cnt+=1
    if n<=0:
        break

if n<0:
    cnt=-1
print(cnt)

