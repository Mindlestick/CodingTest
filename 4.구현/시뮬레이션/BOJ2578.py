# 빙고
def Bingo(g):
    bingo=0 # 빙고 수
    down_diagonal = True
    up_diagonal = True
    for i in range(5):
        # 가로
        if sum(g[i])==0:
            bingo+=1

        # 세로
        sum_length=0
        for j in range(5):
            sum_length+=g[j][i]
            if sum_length>0:
                break
            if j==4 and sum_length==0:
                bingo+=1

        # 하향 대각선
        if down_diagonal and g[i][i]!=0:
            down_diagonal=False

        # 상향 대각선
        if up_diagonal and g[4-i][i]!=0:
            up_diagonal=False

    # 대각선 빙고 있으면 더해주기
    if down_diagonal:
        bingo+=1
    if up_diagonal:
        bingo+=1
    return bingo

g=[[] for i in range(5)]
num=[]
answer=0

for i in range(5):
    g[i]=list(map(int,input().split()))
for i in range(5):
    num+=list(map(int,(input().split())))

for i in range(25):
    # 빙고가 세개 이상이면 멈춤
    if Bingo(g) >= 3:
        answer=i
        break
    for j in range(5):
        # 부른 수가 빙고판에 없으면 넘어가기
        if not num[i] in g[j]:
            continue
        # 있으면 0으로 바꾸기
        else:
            g[j][g[j].index(num[i])]=0

print(answer)