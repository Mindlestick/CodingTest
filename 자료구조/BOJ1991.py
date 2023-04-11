# 트리 순회
def Pre(curr):
    if curr !='.':
        print(curr,end='')
        Pre(tree[curr][0])
        Pre(tree[curr][1])
        
def In(curr):
    if curr !='.':
        In(tree[curr][0])
        print(curr,end='')
        In(tree[curr][1])

def Post(curr):
    if curr !='.':
        Post(tree[curr][0])
        Post(tree[curr][1])
        print(curr,end='')

tree=dict()
n=int(input())
for i in range(n):
    root,left,right=input().split()
    tree[root]=[left,right]

Pre('A')
print()
In('A')
print()
Post('A')