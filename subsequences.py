from itertools import combinations
import time
start = time.process_time()
ip=input()
ip1=input()
lis1=[]
lis2=[]
lis=[]
res=[]
lens=[]
for i in range(len(ip)):
    for j in combinations(ip,i):
        lis1.append("".join(j))
for k in range(len(ip1)):
    for l in combinations(ip1,k):
        lis2.append("".join(l))

for i in lis1:
    if i in lis2:
        lis.append(i)



lis=sorted(lis,key=len,reverse=True)

x=lis[0]
for i in lis:
    if len(i)>=len(x):
        res.append(i)

if len(res)>1:
    for i in res:
        lens.append(lis2.index(i))
if len(lens)>0:
    print(lis2[min(lens)])
else:
    print("X")
end = time.process_time()
print(end - start)
        

