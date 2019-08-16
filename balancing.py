ip=input()
l={"{":"}","[":"]","(":")","<":">"}
c=0
for i in l.keys():
    if i in ip and l[i] in ip:
        c=c+1
print(c)