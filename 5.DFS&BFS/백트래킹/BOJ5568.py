# 카드 놓기
import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
nlist=[]
for i in range(n):
    nlist.append(int(input()))
nlist.sort()
answer=[]
record=[]
num=[0]*100

for i in nlist:
    num[i]+=1

def dfs(start):
    if len(answer)==k:
        #print(' '.join(map(str,answer)))
        s=''.join(map(str,answer))
        if not s in record:
            record.append(s)
        return
    
    for i in range(100):
        if num[i]>0:
            answer.append(i)
            num[i]-=1
            dfs(i)
            answer.pop()
            num[i]+=1

dfs(0)
#print(record)
print(len(record))
