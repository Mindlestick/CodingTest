#럭키 스트레이트

n=input()
l=n[:int(len(n)/2)]
r=n[int(len(n)/2):]
sl=0
sr=0

for i in range(len(l)):
    sl+=int(l[i])
    sr += int(r[i])
if sl==sr:
    print("LUCKY")
else:
    print("READY")
