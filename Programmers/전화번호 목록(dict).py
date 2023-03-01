def solution(phone_book):
    p=dict()
    for i in phone_book:
        for j in range(1,len(i)):
            p[i[:j]]=1
   
    for i in phone_book:
        if i in p:
            return False
    return True