def app(ch,ls):
    l=[]
    for i in numlis:
        if i not in ls:
            l.append(ch+str(i))
    return l
A=input().split()
B=input().split()
C=input().split()
D=input().split()
inum=int(input())
result=[]
numlis=['1','2','3','4','5','6','7','8','9','10']

lA=app("A",A)
lB=app("B",B)
lC=app("C",C)
lD=app("D",D)
if len(lA)>0:
    for a in lA:
        result.append(a)
if len(lB)>0:
    for b in lB:
        result.append(b)
if len(lC)>0:
    for c in lC:
        result.append(c)
if len(lD)>0:
    for d in lD:
        result.append(d)
if len(result)==0:
    print("X")
elif len(result)>=inum:
    print(result[:inum])
else:
    print(result)