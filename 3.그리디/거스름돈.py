n=1260
count = 0

array=[500,100,50,10]

#시간복잡도 = 화폐 개수
for i in array:
    count=count+n//i
    n=n%i

print(count)