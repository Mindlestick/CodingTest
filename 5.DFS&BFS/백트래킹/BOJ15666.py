# N과 M (12)
def dfs(start):
    if m==len(w):
        if not ' '.join(map(str,w)) in answer:
            answer.append(' '.join(map(str,w)))
            print(' '.join(map(str,w)))
        return

    for i in range(start,n):
        w.append(nlist[i])
        dfs(i)
        w.pop()

w=[]
answer=[]
n,m=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
dfs(0)