w = input()
l = {'(': 0, ')': 0}
cnt = 0
for i in w:
    if i == '(':
        if l[')'] == 0:
            cnt += 1
            l['('] += 1
        else:
            l[')'] -= 1
            cnt -= 1
    else:
        if l['('] == 0:
            cnt += 1
        else:
            l['('] -= 1
            cnt -= 1
print(cnt)