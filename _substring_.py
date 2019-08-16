ip=input()
low=ip.lower()
x=""
for i in ip:
    if i.lower() not in x.lower():
        x=x+i
if len(x)>=3:
    print(x)
else:
    print("X")