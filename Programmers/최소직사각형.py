def solution(sizes):
    m,n=0,0
    for i,j in sizes:
        m=max(max(i,j),m)
        n=max(min(i,j),n)
    return m*n