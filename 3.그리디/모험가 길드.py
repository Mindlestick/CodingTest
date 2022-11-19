n=5
data=[2,3,1,2,2]

#n=int(input())
#data=list(map(int,input().split()))
data.sort()

group=0
cnt=0
for i in data:
    cnt+=1
    if cnt==i:
        group+=1
        cnt=0

print(group)