data = "K1KA5CB7"
#ABCKK13

s_list=[]
sum=0
for i in data:
    if i.isnumeric():
        sum+=int(i)
    else:
        s_list.append(i)

s_list.sort()
result=""

for i in s_list:
    result+=i
if sum!=0:
    result = result+str(sum)
print(result)