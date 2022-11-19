n=5
data=['R','R','R','U','D','D']

#n=int(input())
#data = list(map,int(input().split()))

#상하좌우
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move=['U','D','L','R']

x,y = 1,1

for i in data:
    for j in range(len(move)):
        if i == move[j]:
            X = x + dx[j]
            Y = y + dy[j]

    if X < 1 or Y < 1 or X > n or Y > n :
        continue
    x,y = X,Y
print(x,y)
